from urllib.request import urlopen

def get_condition(city):
    url = "https://wttr.in/" + city + "?format=%C"
    page = urlopen(url)
    raw = page.read()
    condition = raw.decode("utf-8")
    return condition

city = input("City: ")
condition = get_condition(city)
f"Weather condition reported for {city} is {condition}"

if condition == "Clear":
    print("No umbrella needed")
else:
    print("Bring an umbrella")
