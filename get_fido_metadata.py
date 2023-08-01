import jwt
import json
import requests

def save_to_json_file(data, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Data saved to {output_file}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def fetch_metadata():
    url = "https://mds3.fidoalliance.org/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        blob = response.text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata from URL: {e}")
        exit(1)

    return blob

def fetch_pub_key():
    url = "http://secure.globalsign.com/cacert/root-r3.crt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        key = response.text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching public key from URL: {e}")
        exit(1)

    return key

if __name__ == "__main__":
    output_file = "fido_metadata.json"

    # fetch metadata
    blob = fetch_metadata()

    # fetch public key (NOT USED CURRENTLY TO VERIFY)
    key = fetch_pub_key()

    # decode the blob
    result = jwt.decode(blob, algorithms=["RS256"], options={"verify_signature": False})

    # save the result
    save_to_json_file(result, output_file)
