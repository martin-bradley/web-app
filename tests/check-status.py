import requests

def ping_url(url):

    try:
        response = requests.get(url)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            print(f'{url} is working.')
        else:
            print(f'{url} returned status code {response.status_code}.')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# Example usage

ping_url('https://www.martinbradley.net')
