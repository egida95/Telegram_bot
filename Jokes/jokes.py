import requests

def get_jokes():
    url = 'https://techrocks.ru/2018/11/28/programmers-jokes-about-themselves/'
    data = requests.get(url).json()
    data = data['<ol>']
    return data

get_jokes("font-weight")

