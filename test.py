from selenium import webdriver
import time
from PIL import Image
import pytesseract
import csv
import requests
from io import BytesIO
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from PIL import ImageEnhance
import re
def change_Image_to_text(img):
    testdata_dir_config = '--tessdata-dir "D://Tesseract-OCR//tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config+' digits')
    # 去掉非法字符，只保留字母数字
    textCode = re.sub("\W", "", textCode)
    return textCode
def htmlcatch(pcode,pname):
        browser.get('http://zs.dgfls.net/zs/Login/index/4')
        input = browser.find_element_by_name('logincode')
        input.send_keys(pcode)
        input = browser.find_element_by_name('password')
        input.send_keys(pname)

        browser.get_screenshot_as_file('screenshot.png')
        element = browser.find_element_by_id('valiCode')
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        im = Image.open('screenshot.png')
        im = im.crop((left, top, right, bottom))

        im=im.convert('L')
        im.save('code.png')

        time.sleep(0.5)
        input = browser.find_element_by_id('authcode')
        pw=change_Image_to_text(im)
        #pw=pytesseract.image_to_string(im,config='--psm 7')
        #print(pw)
        input.send_keys(pw)
        time.sleep(0.5)


        input.send_keys(Keys.ENTER)
        time.sleep(1)
        browser.get('http://zs.dgfls.net/zs/Main/SelScore')
        input=browser.page_source
        soup = BeautifulSoup(input, "html.parser")
        score =soup.find_all('td')
        print(score[2].string.replace(' ','').replace('\n',''))
        browser.get('http://zs.dgfls.net/zs/Main/Logout')
        time.sleep(1)
browser = webdriver.Chrome()
csvfile=open('data.CSV','r',encoding='utf-8')
reader=csv.DictReader(csvfile)
for row in reader:
        print(row['number'],row['name'])
        print(htmlcatch(row['number'],row['name']))
browser.close()
exit(0)
