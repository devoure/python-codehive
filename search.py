#! /usr/bin/python

'''
This is a python script for :
    getting search keywords form the command line
    retrieves the search results page
    opens a browser tab for each result
'''

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception in exc:
    print('There is an issue: \n{}'.format(exc))

soup = bs4.BeautifulSoup(res.text, "html5lib")
linkElems = soup.select('a')
numopens = min(5, len(linkElems))
for i in range(numopens):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
print('THE END')
