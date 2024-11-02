import requests
import time
from data import short_url
def check_website(url, interval=60):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'{url} available')
            else:
                print(f'NOT AVAILABLE, code[{response.status_code}]')
        except requests.ConnectionError:
            print(f'{url} NOT AVAILABLE')
        time.sleep(interval)



check_website(short_url,interval=300)