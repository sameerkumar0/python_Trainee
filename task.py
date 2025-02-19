# from bs4 import BeautifulSoup
# import requests
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# url="https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm"
# res=requests.get(url,headers=headers)
# if res.status_code==200:
#     print(res)
#     soup=BeautifulSoup(res.text,"lxml")


#     page_title=soup.find("h1",id="topic_page_title")
#     print(page_title.text)
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install()) # download and install chrome browser
driver = webdriver.Chrome(service=service)

table_data=[]
url="https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm"
driver.get(url)
print(driver.title)

main=driver.find_element(By.ID,"user_provided")

rows=main.find_elements(By.TAG_NAME,"tr")
for row in rows:
    cols=row.find_elements(By.TAG_NAME,'td')
    data=[col.text for col in cols]
    table_data.append(data)
# print(table_data)

data_extract=pd.DataFrame(table_data)
print(data_extract)


data_extract.to_csv("table_data.csv",index=True)
driver.quit()
