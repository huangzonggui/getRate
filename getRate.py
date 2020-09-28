import requests
import time
from bs4 import BeautifulSoup

import sendMail
import sendMailBySMTP

response = requests.get("http://morate.on9tool.com/?to_currency=%E6%BE%B3%E9%96%80%E5%85%83&from_currency=%E4%BA%BA%E6%B0%91%E5%B9%A3")

soup = BeautifulSoup(response.text, "html.parser")

def getData():
    #  print(item)
    #  bsObj = BeautifulSoup(item, "html.parser")
    #  title = bsObj.find(
    #      "a",
    #      {"class": "btn-rounded"}
    #  )
    #  print(title)
    for link in soup.find_all("a", {"class": "btn-rounded"}):
        print(link.get('data-selected-source'), end = '   ')
        a=link.get('data-selected-rate')
        if a != '':
            print(float(a))
            a = float(a)
            if a >= 0.84488:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>快，換錢啦, 匯率是：', a)
        # print()

#print(soup.prettify())
#  result = soup.find_all("tbody")
#print(result)
#  result = soup.find_all("td")
#print(result)
def test():
    for tr in soup.find_all("tr"):
        # print(type(tr))
        # if len(tr) == 0:
        #     print(tr, 'is null')
        #     break

        tds = tr.findChildren('td', recursive=False)
        # print(type(tds))
        for i in tds:
            # print(type(i.findChidren('a', recursive=False)))
            print(i.findChidren('a', recursive=False))
        
        # for item in tr: 
            # print(item)
            # print(item.string)
            # print(type(item))
            # print(item.find('澳門'))
            # print('======')

# test()
while True: 
    getData()
    print('---------------')
    time.sleep(3)

# sendMail.send()
