import requests
import bs4
city = "Hyderabad"
url = "https://google.com/search?q=sunrise+in+" + city

request_result = requests.get(url)
soup = bs4.BeautifulSoup(request_result.text,"html.parser")
time = soup.find("div", class_='BNeawe' ).text
print(time)