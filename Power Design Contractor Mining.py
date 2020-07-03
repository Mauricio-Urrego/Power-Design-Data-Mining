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
UnitsList = []

driver.get('https://www.powerdesigninc.us/projects/')
#time.sleep(60)
#try:
#    while True:
#        next_page_btn = driver.find_element_by_class_name('btn btn-primary btn--black')
#        if next_page_btn.__sizeof__() <1:
#            print("no more pages left")
#            break
#        else:

NameText = driver.find_elements_by_css_selector('td.title__cell')
for i in NameText:
    NameList.append(i.get_attribute('textContent'))

LocationText = driver.find_elements_by_css_selector('td.location__cell')
for i in LocationText:
    LocationList.append(i.get_attribute('textContent'))

ContractorText = driver.find_elements_by_css_selector('td.gc__cell')
for i in ContractorText:
    ContractorList.append(i.get_attribute('textContent'))

TypeText = driver.find_elements_by_css_selector('td.type__cell')
for i in TypeText:
    TypeList.append(i.get_attribute('textContent'))

UnitsText = driver.find_elements_by_css_selector('td.units__cell')
for i in UnitsText:
    UnitsList.append(i.get_attribute('textContent'))
    
#            next_page_btn.click()
#finally:

#driver.quit()

dict = {'Name': NameList, 'Location': LocationList, 'Type': TypeList, 'Contractor': ContractorList, 'Units': UnitsList}

import pandas as pd

df = pd.DataFrame(dict)

df.to_csv('powerdesigncontractorlist.csv', index=False)

print("done")
