# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

titles = []
authors = []
jur_times = []
read_mores = []
abstracts = []

for i in range(1,9):
    url = 'https://deepmind.com/research/publications/?page={}'.format(str(i))

    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'
    content = web_data.text
    soup = BeautifulSoup(content, 'html.parser')
    print('soup{} done'.format(str(i)))

    titles.extend(soup('h1', class_='h6'))
    print('titles{} done'.format(str(i)))

    authors.extend(soup('span', class_='grey-mid-light'))
    print('authors{} done'.format(str(i)))

    jur_times.extend(soup('p', class_='research-list--item-category p--meta purple-2'))
    print('jur_times{} done'.format(str(i)))

    #read_mores.extend(soup('a', class_='p--meta underline underline--blue-3 link--icon', href="/research/publications/"))
    read_mores.extend(soup('a', class_='p--meta underline underline--blue-3 link--icon', href=re.compile("/research/publications/")))
    print('read more{} done'.format(str(i)))

for read_more in read_mores:
    print(str(read_more.get('href')))
    abs_url = 'https://deepmind.com' + str(read_more.get('href'))
    abs_data = requests.get(abs_url)
    abs_data.encoding = 'utf-8'
    abs_content = abs_data.text
    abs_soup = BeautifulSoup(abs_content, 'html.parser')
    print('an abs content done~')

    abstracts.extend(abs_soup('p'))

titles_fn = 'dm_title_5-8.txt'
authors_fn = 'dm_author_5-8.txt'
jur_times_fn = 'dm_jur_times_5-8.txt'
abs_fn = 'deepmind_abs_5-8.txt'


with open(titles_fn, 'w') as f:
        fo.write(str(titles))
with open(authors_fn, 'w') as f:
        fo.write(str(authors))
with open(jur_times_fn, 'w') as f:
        fo.write(str(jur_times))
with open(abs_fn, 'w') as f:
        fo.write(str(abstracts))

print('all done!!!')
