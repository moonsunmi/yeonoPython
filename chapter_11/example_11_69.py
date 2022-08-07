import urllib.request

url = 'https://python.bakyeono.net'
webpage = urllib.request.urlopen(url).read().decode('utf-8')
print(webpage)