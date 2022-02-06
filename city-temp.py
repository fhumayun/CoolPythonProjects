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