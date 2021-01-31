import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
# 나라별 화폐명 목록가져오기
def get_countries(url):
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
  return countries
# 나라목록 보여주기
def show_country_list(countries):
  for i, country in enumerate(countries):
    print(f"# {i} {country['name']}")

# 나라 선택
def choice():
  try:
    choice = int(input('#: '))

    if choice >= len(countries) or choice < 0:
      print("Choose a number from the list")
      choice()
    else:
      country = countries[choice]
      print(f"{country['name']}\n")
      return country
  except ValueError:
    print("That wasn't a number")
    choice()

def exchange(first, second):
  print(f"How many {first['code']} do you want to convert to {second['code']}")
  
  try:
    input_money = input('#: ')
    url = f"https://transferwise.com/gb/currency-converter/{first['code']}-to-{second['code']}-rate?"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,'html.parser')

    per_money = soup.find('span',{'class':'text-success'}).text

    exchange_money = int(input_money) * float(per_money)

    input_money = format_currency(input_money, first['code'], locale="ko_KR")
    exchange_money = format_currency(int(exchange_money), second['code'], locale="ko_KR")
    
    print(f"{input_money} is {exchange_money}")

  except ValueError as e:
    print("That wasn't a number\n")
    exchange(first,second)
    

countries = get_countries(url)  
show_country_list(countries)

print("Welcome to CurrencyConvert PRO 2000\n")

print("Where are you from? Choose a country by number\n")
first = choice()

print("Now choose another country.\n")
second= choice()

exchange = exchange(first,second)


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
