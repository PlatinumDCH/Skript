import requests

def check_website(url):
    try:
        response = requests.get(url)
        print('Satus code',response.status_code)
        if response.status_code == 200:
            print(f'{url} is normal')
            print('response content',response.text[:500])
        else:
            print(f'{url} is not normal')
    except requests.exceptions.RequestException as err:
        print(f'total error {err}')

