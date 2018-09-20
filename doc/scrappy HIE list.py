import requests
from lxml import etree
import pycountry
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
url = 'https://en.wikipedia.org/wiki/Developed_country'
res = requests.get(url, headers=headers)
selector = etree.HTML(res.text)
infos = selector.xpath('//div[@class="div-col columns column-width"]/ul/li')
names = []
for info in infos:
    names.append(info.xpath('a/text()'))

checkpoint = [index for index, value in enumerate(names) if value == ['Austria']]

names = names[:checkpoint[1]]
dc = []


for i in range(len(names)):
    if len(names[i]) != 0:
        dc.append(names[i][0])


countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

codes = [countries.get(country, 'Unknown code') for country in dc]
codes = set([x for x in codes if x != 'Unknown code'])


# Open File
resultFyle = open("HIE.csv",'w')

# Write data to file
for r in codes:
    resultFyle.write(r + "\n")
resultFyle.close()

