from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
import time

chromedriverpath = r'C:\Users\Maury\AppData\Local\Programs\Python\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_experimental_option("prefs", {
    "download.default_directory": r'C:\Users\Maury\Downloads',
    "download.prompt_for_download": False,
})

driver = webdriver.Chrome(executable_path = chromedriverpath) #, options = options)

NameList = []
LocationList = []
TypeList = []
ContractorList = []
DeveloperList = []
ServicesURLList = []
imageURLList = []

driver.get('https://www.powerdesigninc.us/projects/')
#time.sleep(15)

NameText = driver.find_elements_by_css_selector('p.project__title--small')
for i in NameText:
    NameList.append(i.get_attribute('textContent'))

LocationText = driver.find_elements_by_css_selector('p.project__location--small')
for i in LocationText:
    LocationList.append(i.get_attribute('textContent'))

TypeText = driver.find_elements_by_css_selector('p.project__type')
for i in TypeText:
    TypeList.append(i.get_attribute('textContent'))

ContractorText = driver.find_elements_by_css_selector('p.project__general-contractor')
for i in ContractorText:
    ContractorList.append(i.get_attribute('textContent'))

DeveloperText = driver.find_elements_by_css_selector('p.project__developer')
for i in DeveloperText:
    DeveloperList.append(i.get_attribute('textContent'))

ServicesURLText = driver.find_elements_by_class_name('project__tile')
for i in ServicesURLText:
    ServicesURLList.append(i.get_attribute('data-url'))

imageURLText = driver.find_elements_by_class_name('project__tile')
for i in imageURLText:
    imageURLList.append(i.get_attribute('data-thumb'))

driver.quit()

dict = {'Name': NameList, 'Location': LocationList, 'Type': TypeList, 'Contractor': ContractorList, 'Developer': DeveloperList, 'ServicesURL': ServicesURLList, 'imageURL': imageURLList}

import pandas as pd

df = pd.DataFrame(dict)

df.to_csv('powerdesigncontracts.csv', index=False)

print("done")
