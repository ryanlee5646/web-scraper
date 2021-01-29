import requests
import os

def check_http(url):
  if 'http' not in url:
      url = 'http://' + url
  return url

def check_url():
  print("Welcome to IsItDown.py!")

  urls = input("Please write a URL or URLs you want to check. (sperated by comma)\n").strip().split(',')

  for url in urls:
    url.strip()
    url = check_http(url)

    if '.com' not in url:
      print(f"{url} is not a valid URL")
    
    else: 
      try:
        url_request = requests.get(url)
        if url_request.status_code == 200:
          print(f"{url} is up")    
        
      except:
        print(f"{url} is down!")

  while True:
    ask = input("Do you want to start over? y/n\t")
    if ask == 'y':
      os.system("clear")
      check_url()
      break
    elif ask == 'n':
      print("ok, bye!")
      return
    else:
      print("That's not valid answer.")
    
check_url()