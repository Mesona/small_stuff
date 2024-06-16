import requests

API_KEY="API_KEY_GOES_HERE"

def get_place_id_from_address(address):
    json_data = {
      "textQuery": address,
    }

    headers = {
      "Content-Type": "application/json",
      "X-Goog-Api-Key": API_KEY,
      "X-Goog-FieldMask": "places.id",
    }

    r = requests.post("https://places.googleapis.com/v1/places:searchText", headers=headers, json=json_data)
    return r.json()['places'][0]['id']

def get_place_details_from_id(place_id):
    print("PLACE ID:", place_id)

    headers = {
      "Content-Type": "application/json",
      "X-Goog-Api-Key": API_KEY,
      "X-Goog-FieldMask": "id,displayName,nationalPhoneNumber,internationalPhoneNumber,websiteUri",
    }

    r = requests.get(f"https://places.googleapis.com/v1/places/{place_id}", headers=headers)
    print("R:", r)
    print("R JSON:", r.json())

def get_place_details_from_id_old_api(place_id):
    print("PLACE ID:", place_id)

    params = {
      'place_id': place_id,
      'fields': 'name,website,formatted_phone_number',
      'key': API_KEY,
    }

    r = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=params)

    return r.json()

super_duper_burger = 'ChIJwyMuoFa1j4ARM-FHAbUNfjI'
google = 'ChIJN1t_tDeuEmsRUsoyG83frY4'

place_id = get_place_id_from_address("5399 Prospect Rd, San Jose, CA 95129")
print(get_place_details_from_id(place_id))
