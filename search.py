#coding:utf-8
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup 
import sys

da = sys.argv[1].split('1216')
url = 'http://www.xiami.com/search/song/page/' + da[0] + '?key=' + da[1]
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}  
response = urllib.request.urlopen(urllib.request.Request(url=url,headers=headers))
soup = BeautifulSoup(response.read(),'lxml')
main = soup.find(class_='result_main')
page = soup.find(class_='all_page')
data = {}

i = 0
for id in main.findAll('input',{'name': 'recommendids'}):
    data[i] = id.get('value').replace(' ','') + '-=-'
    i += 1

i = 0
for a in main.findAll('td',{'class': 'song_name'}):
    data[i] += a.text.replace('MV','').replace('\n','').replace(' ','').replace('\r','').replace('\t','')   + '-=-'
    i += 1

i = 0
for a in main.findAll('td',{'class': 'song_artist'}):
    data[i] += a.text.replace('\n','').replace(' ','').replace('\r','').replace('\t','') + '-=-'
    i += 1

i = 0
for a in main.findAll('td',{'class': 'song_album'}):
    data[i] += a.text.replace('\n','').replace(' ','').replace('\r','').replace('\t','')
    i += 1

de = ''
for ii in range(0,len(data)):
    de += data[ii] + '=-='

de = de[:-3] + '=||='
for aa in page.findAll('a'):
    de += aa.text + '-=-'

de += page.find('span').text + '-=-' + page.findAll('a',{'class': 'p_curpage'})[0].text

print(urllib.parse.quote(de))