from urllib.request import urlopen

url = "https://www.metoffice.gov.uk/weather/forecast/u10mr8xus#?nearestTo=SS0"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)