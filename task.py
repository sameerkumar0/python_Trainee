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
# import pandas as pd 
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager



# service = Service(ChromeDriverManager().install()) # download and install chrome browser
# driver = webdriver.Chrome(service=service)

# table_data=[]
# url="https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm"
# driver.get(url)
# print(driver.title)

# main=driver.find_element(By.ID,"user_provided")

# rows=main.find_elements(By.TAG_NAME,"tr")
# for row in rows:
#     cols=row.find_elements(By.TAG_NAME,'td')
#     data=[col.text for col in cols]
#     table_data.append(data)
# # print(table_data)

# data_extract=pd.DataFrame(table_data)
# print(data_extract)


# data_extract.to_csv("table_data.csv",index=True)
# driver.quit()


import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup and initialize the WebDriver with explicit wait
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)  # 10 seconds wait time

try:
    url = "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm"
    driver.get(url)
    print(driver.title)

    # Wait for the table to be present
    main = wait.until(EC.presence_of_element_located((By.ID, "user_provided")))

    # Extract rows
    rows = main.find_elements(By.TAG_NAME, "tr")
    table_data = []

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        if cols:  # Avoid empty rows or header rows if they're different
            data = [col.text for col in cols]
            table_data.append(data)

    # Convert to DataFrame
    data_extract = pd.DataFrame(table_data, columns=None)  # Optionally define column names if known

    # Clean data: remove empty rows if any
    data_extract = data_extract.dropna(how='all').reset_index(drop=True)

    # Output data
    print(data_extract)
    data_extract.to_csv("table_data.csv", index=False)  # Index might not be needed

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
