import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
trs = soup.find_all("tr")
nations = []

print("Hello! Please choose select a country by number:")

for tr in trs[1:]:
  tds = tr.find_all("td")
  if tds[1].text != "No universal currency":
    nations.append([tds[0].text,tds[2].text])  

for i,j in enumerate(nations):
  print(f'# {i} {j[0].capitalize()}')

while True:
  answer = input('#: ')
  try:
    answer = int(answer)
    if answer > i:
      print("Choose a number from the list")
    else:
      print(f"You chose {nations[answer][0].capitalize()}\nThe currency code is {nations[answer][1]}")
      break
  except:
    print("That wasn't a number")