from bs4 import BeautifulSoup
import re
import requests
import webbrowser


url = input("1001 Tracklists URL you want to find DL links for: ")
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
results = BeautifulSoup(response.content, 'lxml')

track_list = []
tracks = results.findAll('meta', {'itemprop' : 'name'})
for track in tracks:
    track_list.append(track['content'])

for track in track_list:
    new = 2
    tabUrl = "http://google.com/search?q="
    term = track + "+zippyshare" # searching for matching zippyshare link
  
    webbrowser.open(tabUrl + term,new = new)
