import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = 'https://campus.quipper.com/directory'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive alll of the ancor tags

tags = soup('a')

print(html)
for tag in tags:
    print(tag)