import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from twilio.rest import Client
import pickle

site = "https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J1CPD1/ref=lp_22429860031_1_2?s=electronics&ie=UTF8&qid=1606104936&sr=1-2"
headers = {
     "User-Agent": "C:/chromedriver.exe"
}

response=requests.get(site,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
def check_price():
     title=soup.find(id="productTitle").get_text()
     price=soup.find(id="priceblock_ourprice").get_text().strip()
     print("Product name & specs : ",title.strip())
     print("Product cost:",price)
     stripped_price = price.strip("₹ ,")
     replaced_price = stripped_price.replace(",", "")
     find_dot = replaced_price.find(".")
     to_convert_price = replaced_price[0:find_dot]
     converted_price = int(to_convert_price)
     return converted_price

def msg(password):
     num='+919944446313'
     client = Client("AC47902c9d8bcc3e1388601d2595023044", "bcc68cd2d28f9ef27e9fc0e2d3be6da5")
     client.messages.create(from_='+17706912470',
                           to=num,
                           body='The Price is : '+password)
    
def get_price(price):
     html = requests.get(site, headers=headers).text
     soup = BeautifulSoup(html, 'html.parser')
     price1 = [i.get_text() for i in
             soup.find_all('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})]
     final_price = ''.join(price1)[2:8]
     final_price = int(final_price.replace(',', ''))
     if final_price < price | final_price > price :
          cp='Price changed '+str(price)+' to '+str(final_price)
          print(cp)
          msg(cp)
          print('Message sent')
     else:
          pr='Same Price '+str(price)
          print(pr)
          msg(pr)
          print('Message sent')
a=check_price()

while True:
     count=0
     get_price(a)
     time.sleep(60)
