"""Case-study #4 Парсинг web-страниц
Developers: Revtova L. (%)
            Arkhipova A. (%)

"""
import urllib.request
elements = []
out_file = open('output.txt', 'w')
with open('input.txt', 'r') as inp_file:
    line = inp_file.readlines()
for url in line:
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)
    part_name = text.find("player-name")
    name = text[text.find('>',part_name)+1:text.find('&',part_name)]

T = 'total'
total = text.find(T)
text = text[total:] #нахожу тотал и обрезаю все до тотала
text = text[text.find('L') + 1:]

text = text.replace('\\n', '') #убираю слеш н
text = text.replace('\\t', '') #убираю слеш т
text = text.replace('td', '') #убираю тд
text = text.replace('<', '')
text = text.replace('/', '')
text = text[2:]
text = text[:text.find('tr')]
text = text.replace('>', ' ')
print(text)

for i in range(10):
    c = text[:text.find('  ')]
    elements.append(c)
    text = text[text.find('  ') + 1:]
print(elements)
