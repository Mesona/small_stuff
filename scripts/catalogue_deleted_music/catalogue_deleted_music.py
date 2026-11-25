import os
import shutil

from pathlib import Path

PHONE="/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_R5CT8116HAA/Internal storage/Music/"
SOURCE="/media/mesona/SlowerGames/TEMPORARY WATER STORAGE/Music/"
DELETED_BACKUP=SOURCE + "RemovedFromDevice/"

def main():
    detect_and_move_deleted_music()

def detect_and_move_deleted_music():
    for root, directories, files in os.walk(SOURCE):
        for file in files:
            if "RemovedFromDevice" in root:
                continue

            directory = root.replace(SOURCE, "")
            phone_absolute = PHONE + directory + "/" + file
            source_absolute = root + "/" + file

            if not os.path.exists(phone_absolute):
                # print(phone_absolute)
                # print(source_absolute)
                backup = DELETED_BACKUP + directory

                # print(backup)
                os.makedirs(backup, exist_ok=True)

                shutil.move(source_absolute, backup)

main()
