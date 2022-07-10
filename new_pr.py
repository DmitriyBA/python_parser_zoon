import csv
from itertools import dropwhile
from lib2to3.pgen2 import driver
from operator import delitem
from re import I
from selenium.webdriver.common.keys import Keys
from stringprep import in_table_a1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
# import requests
# from bs4 import BeautifulSoup as bs
# import json

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
]

option = webdriver.ChromeOptions()
option.add_argument(f"user-agent={random.choice(user_agent)}")

driver = webdriver.Chrome(executable_path="C:\\Users\\Shhhn\\OneDrive\\Рабочий стол\\web_menu\\selenium_parser\\chromedriver_win32\\chromedriver.exe", options=option)

def scroll(): 
    while True: 
        scroll_down = driver.find_element_by_class_name('_1rkbbi0x')
        if(driver.find_elements_by_class_name('_1x4k6z7')):
            break
        else:
            action = ActionChains(driver)
            action.move_to_element(scroll_down).perform()
            time.sleep(1)
            
def scrap():
    url_item = driver.current_url
    driver.get(url=url_item)
    
def blocks_get(block_page):
    url_link = []
    for item in block_page:
        time.sleep(1)
        item.click()
        url_item = driver.current_url
        url_link.append(url_item)
        time.sleep(1)
        scroll()
    return url_link

def next():
    button_next = driver.find_element_by_class_name('_n5hmn94') #вперед
    button_next.click()

for i in range(1,): #здесь нужно ввести вместо 98 количество страниц для парсинга
    url = f"https://2gis.ru/moscow/search/%D0%A4%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D0%BD%D0%B3/rubricId/1236/page/{i}"
    driver.get(url=url)
    time.sleep(2)
    items = driver.find_elements_by_xpath("//div[@class='_1h3cgic']")
    url_links = blocks_get(items)
    next()

results_list = []

for link_item in url_links:
    driver.get(url=link_item)
    
    try: 
        name = driver.find_element_by_class_name("_oqoid").text.strip()
    except Exception as _error:
         name = None
         
    try:
        work_profession = driver.find_element_by_class_name("_oqoid").text
    except Exception as _error:
        work_profession = None
    
    phone_list = []
    try:
        phones = driver.find_elements_by_xpath("//a[@class='_2lcm958']")
        phone_list.append(str(phones))
    except Exception as _error:
        phone_list = None 
        
    try:
        site = driver.find_element_by_class_name("_1rehek").text
    except Exception as _error:
        site = None
        
    try:
        email = driver.find_element_by_class_name("_2lcm958").text
    except Exception as _error:
        email = None
        
    results_list.append(
         {
             "NAME": name,
             "PHONES": phone_list,
             "SITE": site,
             "WORK": work_profession,
             "EMAIL": email,
             "URL": link_item
         }
     )
    
    time.sleep(random.randrange(1, 3))

with open("contact.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "Name", 
            "Phones", 
            "Web-site",
            "Work company", 
            "Email", 
            "Link"
        )
    )
    
    for item_info in results_list:
        
        info_name = item_info["NAME"]
        info_phones = item_info["PHONES"]
        info_website = item_info["SITE"]
        info_work_company = item_info["WORK"]
        info_email = item_info["EMAIL"]
        info_url = item_info["URL"]
        
        with open("contact.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(
                (info_name, 
                info_phones, 
                info_website,
                info_work_company,
                info_email,
                info_url)
            )

time.sleep(10)
driver.close()
driver.quit()

