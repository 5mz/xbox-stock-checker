from bs4 import BeautifulSoup
from datetime import datetime
import requests
import webbrowser
import time

URL_AMAZON = 'https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_3?keywords=xbox+series+x+console&qid=1645156829&sr=8-3'
URL_MICROSOFT2 = 'https://www.xbox.com/en-US/consoles/xbox-series-x?cid=msft_web_collection'
URL_GAMESTOP = 'https://www.gamestop.com/consoles-hardware/xbox-series-x%7Cs/consoles/products/microsoft-xbox-series-x/11108371.html?bt=true'
check = True
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.112 Safari/537.36'}

# change application path to whatever yours is 
webbrowser.register('Brave', None, webbrowser.BackgroundBrowser("C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe")) 
session = requests.Session()

def makeRequest(provider):
    page = session.get(provider, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')
timer = 0
while check == True:
    sleep = int()
    timer = timer + 1
    if timer == 100:
        session = requests.Session()
        timer = 0

    requestAmazon = makeRequest(URL_AMAZON)
    resultsAmazon = requestAmazon.find(id='add-to-cart-button')

    if 'Series X' not in requestAmazon.text:
        print('Amazon check failed at:\t\t\t', datetime.now().strftime("%H:%M:%S"))
        session = requests.Session()
    elif resultsAmazon != None:
        webbrowser.get('Brave').open(URL_AMAZON)
        print('XBOX FOUND ON AMAZON!')
        exit()
    elif 'Series X' in requestAmazon.text:
        print('Amazon check successful at:\t\t', datetime.now().strftime("%H:%M:%S"))
    else:
        print('Unknown error on Amazon:\t', datetime.now().strftime("%H:%M:%S"))
		
    requestMS = makeRequest(URL_MICROSOFT2)
    if requestMS.find(id='buttons_AddToCartButton') != None or requestMS.find(id='buttons_ConfigureDeviceButton') != None: 
        webbrowser.get('Brave').open(URL_MICROSOFT2)
        print('XBOX FOUND on Microsoft!')
        exit()
    else:
        print('Microsoft check successful at:\t', datetime.now().strftime("%H:%M:%S"))

    requestMS = makeRequest(URL_GAMESTOP)
    if requestMS.find(id='buttons_AddToCartButton') != None or requestMS.find(id='buttons_ConfigureDeviceButton') != None: 
        webbrowser.get('Brave').open(URL_GAMESTOP)
        print('XBOX FOUND on GAMESTOP!')
        exit()
    else:
        print('Gamestop check successful at:\t', datetime.now().strftime("%H:%M:%S"))
