import requests
from bs4 import BeautifulSoup
import json
import time

headers={
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'  
}
q = 0
for q in range(1,51):
    q +=1
    url = f'https://www.cian.ru/cat.php?currency=2&deal_type=sale&district%5B0%5D=21&engine_version=2&minprice=100000000&offer_type=flat&p={q}'

    link_list = []
    result = []


    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    # with open('циан/циан.html', 'w', encoding='utf-8') as file:
    #     file.write(req.text)

    link = soup.find_all(class_='_93444fe79c--content--lXy9G')
    for i in link:
        link_list.append(i.find('a').get('href'))

    for url_2 in link_list:
        req_2 = requests.get(url_2, headers=headers)
        soup = BeautifulSoup(req_2.text, 'lxml')
        try:
            time.sleep(2)
            name = soup.find(class_='a10a3f92e9--link--A5SdC').text.replace(" ", "")
        except AttributeError:
            name = '-'        
        try:
            time.sleep(2)
            price = soup.find(class_='a10a3f92e9--amount--ON6i1').text.replace(" ", ".")
        except AttributeError:
            price = '-'
        try:
            time.sleep(2)
            square = soup.find(class_='a10a3f92e9--color_black_100--Ephi7 a10a3f92e9--lineHeight_6u--cedXD a10a3f92e9--fontWeight_bold--BbhnX a10a3f92e9--fontSize_16px--QNYmt a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY').text.replace(" ", "")
        except AttributeError:
            square = '-' 
            
        try:
            time.sleep(2)
            ip = soup.find(class_='a10a3f92e9--address-line--GRDTb').text.replace(" ", "")
            ip = ip.replace("На карте", "")
        except AttributeError:
            ip = '-' 

        result.append({
            'Название':name,
            'Цена': price,
            'Общая площадь': square,
            'адрес':ip,
            'url':url_2
        })

        with open('циан/циан.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    link_list = []
    result = []
