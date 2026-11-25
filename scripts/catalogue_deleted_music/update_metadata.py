import os
import json
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, TCON
from openai import OpenAI

# --- CONFIGURATION ---
client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

MODEL_NAME = "llama3" # Change to your preferred local model
MUSIC_DIR = "/home/mesona/Downloads/NotYetCleanedMusic/AITest"

def get_metadata_from_ai(title, artist):
    """Calls the AI to get corrected metadata."""
    prompt = f"""
    Provide accurate music metadata for the song: "{title}" by "{artist}".
    Return the result strictly as a JSON object with these keys:
    "Title", "Artist", "Album", "Year", "Genres" (as a comma-separated string).
    Do not include any conversational text, only the JSON.
    """
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        data = json.loads(response.choices[0].message.content)
        return {
            "Title": data.get("Title"),
            "Artist": data.get("Artist"),
            "Album": data.get("Album"),
            "Year": data.get("Year"),
            "Genres": data.get("Genres")
        }
    except Exception as e:
        print(f"  [AI Error] Could not fetch metadata for {title}: {e}")
        return None

def update_file_metadata(file_path, metadata):
    """Writes metadata back to the file. Returns True if successful, False otherwise."""
    try:
        audio = MP3(file_path, ID3=ID3)

        # Clear existing tags to ensure a clean update (optional but recommended)
        # audio.tags.clear()

        audio.tags.add(TIT2(encoding=3, text=metadata["Title"]))
        audio.tags.add(TPE1(encoding=3, text=metadata["Artist"]))
        audio.tags.add(TALB(encoding=3, text=metadata["Album"]))
        audio.tags.add(TYER(encoding=3, text=metadata["Year"]))

        genres = [g.strip() for g in metadata["Genres"].split(",")]
        audio.tags.add(TCON(encoding=3, text=genres[0]))

        audio.save()
        return True
    except Exception as e:
        print(f"  [Write Error] Could not save tags to {file_path.name}: {e}")
        return False

def main():
    path = Path(MUSIC_DIR)
    failed_files = [] # List to store (file_path, reason, metadata_received)

    # Process only .mp3 files
    files = list(path.glob("*.mp3"))
    print(f"Found {len(files)} files. Starting processing...\n")

    for file_path in files:
        filename = file_path.stem
        if " - " in filename:
            artist_guess, title_guess = filename.split(" - ", 1)
        else:
            artist_guess = "Unknown"
            title_guess = filename

        print(f"Processing: {title_guess} by {artist_guess}...")

        metadata = get_metadata_from_ai(title_guess.strip(), artist_guess.strip())

        if metadata:
            success = update_file_metadata(file_path, metadata)
            if not success:
                # Case: AI gave us data, but disk write failed
                failed_files.append({
                    "file": file_path.name,
                    "reason": "Write Error",
                    "metadata": metadata
                })
        else:
            # Case: AI failed to provide metadata
            failed_files.append({
                "file": file_path.name,
                "reason": "AI Fetch Error",
                "metadata": None
            })

    # --- FINAL SUMMARY REPORT ---
    print("\n" + "="*50)
    print("PROCESSING COMPLETE")
    print("="*50)

    if not failed_files:
        print("Success! All files were updated successfully.")
    else:
        print(f"Found {len(failed_files)} failure(s):")
        for fail in failed_files:
            print(f"\nFile: {fail['file']}")
            print(f"Reason: {fail['reason']}")
            if fail['metadata']:
                print(f"Metadata received from AI: {fail['metadata']}")
            else:
                print("Metadata received from AI: N/A")

    print("="*50)

if __name__ == "__main__":
    main()
