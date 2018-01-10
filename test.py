import urllib2

url = "https://www.msn.com/en-in/weather/today/ludhianapunjabindia/we-city?q=ludhiana-punjab&form=PRWLAS&iso=IN&el"
response = urllib2.urlopen(url)
source = response.read()
print(source)
