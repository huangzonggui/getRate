import requests
import time
import sys
from bs4 import BeautifulSoup

import sendMail
import sendMailBySMTP

response = requests.get("http://morate.on9tool.com/?to_currency=%E6%BE%B3%E9%96%80%E5%85%83&from_currency=%E4%BA%BA%E6%B0%91%E5%B9%A3")

soup = BeautifulSoup(response.text, "html.parser")

expectExchangeRate = 0.89
nowRate = 0
sendOrNot = False

def changeExpectExchangeRate(): 
    global expectExchangeRate
    try:
        print(float(sys.argv[1]))
        expectExchangeRate = float(sys.argv[1])
    except Exception:
        print('changeExpectExchangeRate error')

def getRatesTable(): 
    # print(soup.find(id='rates'))
    rateTable = soup.find(id='rates')
    # print(rateTable.tbody)
    # print(rateTable.tbody.tr)
    # print(rateTable.tbody.find_all("img"))
    allImg = rateTable.tbody.find_all("img")
    # img_urls = []
    for oneImg in allImg: 
        # img_urls.append(oneImg['src'])
        oneImg['src'] = 'https://morate.on9tool.com' + oneImg['src']
    # print(rateTable.tbody.find(text="/images/").replaceWith("https://morate.on9tool.com/images/"))
    # print(rateTable)
    # print(img_urls)
    # img_urls = ['https://morate.on9tool.com' + sub for sub in img_urls]
    # print(img_urls)

    allTh = rateTable.thead.find_all("th")
    for oneTh in allTh: 
        # oneTh['style'] = "color: red;"
        oneTh['style'] = "text-align: left;color: red;"
    # print(allTh)

    # print(rateTable)
    return rateTable

def getData():
    global sendOrNot
    #  print(item)
    #  bsObj = BeautifulSoup(item, "html.parser")
    #  title = bsObj.find(
    #      "a",
    #      {"class": "btn-rounded"}
    #  )
    #  print(title)

    changeExpectExchangeRate()
    print('expectExchangeRate:', expectExchangeRate)

    for link in soup.find_all("a", {"class": "btn-rounded"}):
        print(link.get('data-selected-source'), end = '   ')
        a=link.get('data-selected-rate')
        if a != '':
            print(float(a))
            a = float(a)

            if a >= expectExchangeRate:
                sendOrNot = True
                nowRate = a
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>快，換錢啦, 匯率是：', a)
        # print()

    if sendOrNot: 
        sendMailBySMTP.send(nowRate, getRatesTable())

def test():
    for tr in soup.find_all("tr"):
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

while True: 
    getData()
    print('---------------')
    time.sleep(60*60*24)

# getRatesTable()

# getData()

# sendMailBySMTP.send()
# sendMail.send()
