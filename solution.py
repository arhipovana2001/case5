"""Case-study #4 Парсинг web-страниц
Developers: Revtova L. (60%)
            Arkhipova A. (55%)
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
        name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

        T = 'total'
        total = text.find(T)
        text = text[total:]
        text = text[text.find('L') + 1:]
        text = text.replace('\\n', '')
        text = text.replace('\\t', '')
        text = text.replace('td', '')
        text = text.replace('<', '')
        text = text.replace('/', '')
        text = text[2:]
        text = text[:text.find('tr')]
        text = text.replace('>', ' ')
        text = text.replace(',', '.')

        for i in range(10):
            c = text[:text.find('  ')]
            elements.append(c)
            text = text[text.find('  ') + 2:]

        COMP = '{0:<7.4}'.format(elements[0])
        ATT = '{0:<7.4}'.format(elements[1])
        YDS = '{0:<7.4}'.format(elements[3])
        TD = '{0:<7.4}'.format(elements[5])
        INT = '{0:<7.4}'.format(elements[6])
        RATE = '{0:<7.5}'.format(elements[9])
        name = name + ' ' * (20 - len(name))
        COMP = COMP + ' ' * (7 - len(COMP))
        ATT = ATT + ' ' * (7 - len(ATT))
        YDS = YDS + ' ' * (7 - len(YDS))
        TD = TD + ' ' * (7 - len(TD))
        INT = INT + ' ' * (7 - len(INT))
        RATE = RATE + ' ' * (7 - len(RATE))
        out_file.write('{}{}{}{}{}{}{}'.format(name, COMP, ATT, YDS, TD, INT, RATE))
        out_file.write('\n')
        elements = []
out_file.close()
