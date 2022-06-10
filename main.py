import csv

import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
headers = {
    'accept': '*/*',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safa"
}
url = 'https://www.mealty.ru/catalog/'
reg = requests.get(url, headers=headers)
src = reg.text

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(src)

with open("index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

items = soup.find_all(class_='catalog-item')
dict_items = []
for item in items:
    item_dict = {}
    item_dict['name'] = item.find(class_='meal-card__name').text + item.find(class_='meal-card__name-note').text
    item_dict['description'] = item.find(class_="meal-card__description").text
    item_dict['weight'] = item.find(class_='meal-card__weight').text
    item_dict['proteins'] = item.find(class_='meal-card__proteins').text
    item_dict['fats'] = item.find(class_='meal-card__fats').text
    item_dict['carbohydrates'] = item.find(class_='meal-card__carbohydrates').text
    item_dict['calories'] = item.find(class_='meal-card__calories').text
    item_dict['products'] = item.find(class_='meal-card__products').text
    item_dict['price'] = item.find(class_='basket__footer-total-count').text
    dict_items.append(item_dict)


with open('out.csv', 'w', encoding='utf-8', newline="") as out:
    field_names = ['name', 'description', 'weight', 'proteins', 'fats', 'carbohydrates', 'calories', 'products', 'price']
    writer = csv.DictWriter(out, field_names)
    writer.writeheader()
    for item in dict_items:
        writer.writerow(item)



