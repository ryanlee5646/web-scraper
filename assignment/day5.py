import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
trs = soup.find_all("tr")[1:]
countries = []

for tr in trs:
  tds = tr.find_all("td")
  name = tds[0].text
  currency = tds[1].text
  code = tds[2].text

  if currency != "No universal currency":
      country = {
          'name': name.capitalize(),
          'code': code
      }
      countries.append(country)  

print("Hello! Please choose select a country by number:")
for i, country in enumerate(countries):
  print(f"# {i} {country['name']}")

def ask():
  try:
    choice = int(input('#: '))

    if choice >= len(countries) or choice < 0:
      print("Choose a number from the list")
      ask()
    else:
      country = countries[choice]
      print(f"You chose {country['name']}\nThe currency code is {country['code']}")
  except ValueError:
    print("That wasn't a number")
    ask()

ask()