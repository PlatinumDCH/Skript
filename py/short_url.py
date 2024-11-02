import requests
import sys

def shorten_url_with_tiny(long_url):
    url = f'http://tinyurl.com/api-create.php?url={long_url}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

if __name__ == '__main__':
    my_url = sys.argv[1]
    short_url = shorten_url_with_tiny(my_url)
    if short_url:
        print('Shorted URL',short_url)
    else:
        print('Error shorting URL')