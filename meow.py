from bs4 import BeautifulSoup


with open('base.html', encoding='utf-8') as f:
    src = f.read()


bs = BeautifulSoup(src, 'lxml')

print(bs)