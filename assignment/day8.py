import os
import csv
import requests
from bs4 import BeautifulSoup

def get_company(url):
    companies_request = requests.get(url)
    companies_soup = BeautifulSoup(companies_request.text,'html.parser')
    html = companies_soup.find("div",{"id":"NormalInfo"})

    datas = html.find_all("tr")
    companies = []

    for data in datas:
        try:
            place = data.find("td", {"class":"local first"})
            if place == None:
                continue
            else:
                place = place.get_text().replace("\xa0", " ", 1)
            title = data.find("span",{"class":"company"}).string
            time = data.find("span", {"class":"time"})

            if place == None:
                continue
            else:
                time = time.string
            pay = data.find("td",{"class":"pay"}).string 
            date = data.find("td",{"class": "regDate last"}).string
            companies.append({
                "place" : place,
                "title" : title,
                "time"  : time,
                "pay" : pay,
                "date" : date
            })
            
        except:
            pass
    return companies        

def save_file(company,jobs):
    file = open(f"file/{company}.csv", mode="w") # mode를 쓰기만 설정해줌
    writer = csv.writer(file)
    writer.writerow(['place','title','time','pay','date'])
    
    # job은 dictionary 형태이다. -> list형태로 변형 필요
    for job in jobs:
        writer.writerow(list(job.values()))
    return


os.system("clear")
alba_url = "http://www.alba.co.kr"

request = requests.get(alba_url)
soup = BeautifulSoup(request.text, 'html.parser')

cards = soup.find_all("li", {"class":"impact"})

companies = []

for card in cards:
    company = card.find("span",{"class":"company"}).text
    url = card.find('a',{'class':"goodsBox-info"})["href"]
    
    jobs = get_company(url)
    
    save_file(company,jobs)



