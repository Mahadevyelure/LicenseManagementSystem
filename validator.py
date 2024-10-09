import requests

SERVER_URL = 'http://127.0.0.1:5000'

def validate_license(license_key):
    try:
        response = requests.post(f'{SERVER_URL}/validate', json={'license_key': license_key})
        if response.status_code == 200:
            print("License is valid.")
        else:
            print("License is invalid:", response.json().get('message'))
    except requests.exceptions.RequestException as e:
        print("Error connecting to the license server:", e)

if __name__ == '__main__':
    license_key = 'example-license-key-82918291'
    validate_license(license_key)
