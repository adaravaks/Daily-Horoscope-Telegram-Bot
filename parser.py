import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()


def get_signs_and_urls():
    url = 'https://horo.mail.ru/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    signs_raw = soup.find_all('div', class_='cols__column_small_percent-25')
    signs = {}

    for sign in signs_raw:
        sign_name = sign.find('span', class_='p-imaged-item__name').text.lower()
        sign_page_url = url + sign.find('a', class_='p-imaged-item_circle').get('href')
        signs[sign_name] = sign_page_url

    return signs


def get_horoscope(sign_name):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    signs = get_signs_and_urls()
    response = requests.get(signs[sign_name], headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    horoscope_text = soup.find('div', class_='article__item_alignment_left').text
    return horoscope_text


if __name__ == '__main__':
    user_sign = input('Введите свой знак зодиака: ').lower().strip()
    try:
        print(get_horoscope(user_sign))
    except Exception as ex:
        print(f'Я не нашёл гороскопа для знака {user_sign}')
