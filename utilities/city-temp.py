import ssl

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
    
from urllib.request import urlopen

def get_temp(city):
    url = "https://wttr.in/" + city + "?format=%t"
    page = urlopen(url)
    raw = page.read()
    temp = raw.decode("utf-8")
    return temp

city = input("City: ")
temp = get_temp(city)

print(temp)