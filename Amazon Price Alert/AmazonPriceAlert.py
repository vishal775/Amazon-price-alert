# Before running this code go to www.twilio.com and create a account with your PHONE NUMBER and get a TRIAL NUMBER for your account by your choice.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from twilio.rest import Client
import pickle

# Choose the Product and copy the Product URL and paste it in site = "Product URL" given below
site = "https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J1CPD1/ref=lp_22429860031_1_2?s=electronics&ie=UTF8&qid=1606104936&sr=1-2"

# Download Chrome Driver by checking the version of the chrome you are using 
# After Download extract in Local Disc C if possible or any other Local Disc.
# Now get the whole PATH of chromediver.exe in extracted directory and paste it in "User-Agent": "YOUR CHROMEDRIVER.EXE PATH"
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

# Enter your Phone Number.
# Get the YOUR_ACCOUNT_SID and YOUR_AUTH_TOKEN by logging in your Twilio Account and paste in Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN") mentioned below.
# Get your Trail Number which you can see in the Dashboard and enter it in from_='YOUR_TRIAL_NUMBER' given below.
def msg(password):
     num='+91'+'YOUR_PHONE_NUMBER'
     client = Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")
     client.messages.create(from_='YOUR_TRIAL_NUMBER',
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
          
          # If needed you can get the Message for the same price also 
          #msg(pr)
          #print('Message sent')
          
a=check_price()

while True:
     count=0
     get_price(a)
     time.sleep(60) # You can change the 60 according to your needed refresh time of your Product so that it gives the exact price of it.
