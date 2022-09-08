#pip install requests beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
cookies = {'adbsess' : 'dThTFyXwOzeKaCjI',
           'adbautopass' : 'vqervhKHeHjUGhUC',
           'adbss' : '834194-dThTFyXw',
           'adbautouser' : 'ghdus9037',
           'anidbsettings' : '%7B%22USEAJAX%22%3A1%7D',
           'adbsessuser' : 'ghdus9037',
           'adbuin' : '1515322662-qmCt'}
target_url = "http://anidb.net/anime/11046"

request = urllib.request.Request(url=target_url, headers=headers)
req = urllib.request.urlopen(request)

bsObject = BeautifulSoup(req.read(), "html.parser")

items = bsObject.select("#anidb > #layout-content > #layout-main > div")

for item in items:
    print(item)