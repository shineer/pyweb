#coding:utf-8
import urllib.request
import urllib.parse
import time
import sys
import json

t = str(int(time.time() * 1000))
url = 'http://www.xiami.com/song/playlist/id/' + sys.argv[1] + '/object_name/default/object_id/0/cat/json?_ksTS=' + t + '_389&callback=jsonp390'
headers = { 'Referer': 'http://www.xiami.com/play?ids=/song/playlist/id/'+ sys.argv[1] +'/object_name/default/object_id/0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
            }  
response = urllib.request.urlopen(urllib.request.Request(url=url,headers=headers) )
data = json.loads(response.read().decode('utf-8').replace('jsonp390(','').replace(')',''))['data']['trackList'][0]
ciphertext = data['location']
totle = int(ciphertext[0:1])
new_str = ciphertext[1:]
chu = int(len(new_str)/int(totle))
yu = len(new_str) % totle
stor = {}
i = 0
while i<yu:
	index = (chu+1)*i
	length = chu+1
	stor[i] = new_str[index:index+length]
	i+=1
i = yu
while i<totle:
	index = chu*(i-yu)+(chu+1)*yu
	length = chu
	stor[i] = new_str[index:index+length]
	i+=1
pin_str = ""
for ii in range(0,len(stor[0])):
	for jj in range(0,len(stor)):
		pin_str += stor[jj][ii:ii+1]
print(urllib.parse.unquote(pin_str).replace('^', '0') + '-=-' + data['lyric'] + '-=-' + data['pic'])