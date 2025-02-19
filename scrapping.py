from bs4 import BeautifulSoup
import requests
import pandas as pd

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=28b62c9d-1a5f-458f-b337-126ea2011cdd&as-backfill=on"
# response=requests.get(url)
# if response.status_code==200:
#     print(response)
#     soup=BeautifulSoup(response.text,'lxml')
#     print(soup)
#     # text=soup.get_text()
#     # print(text.strip())
# else:
#     print("Failed to load data ")

# title = soup.title.text
# print("Page Title:", title)


# H1=soup.find('h1') # to get the one h1
# print(H1)

# h1=soup.find_all('div')
# for headings in h1:
#     print(headings)

# for i in range(2,10):
#     url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=28b62c9d-1a5f-458f-b337-126ea2011cdd&as-backfill=on&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&page="+str(i)
#     r=requests.get(url)
#     print(r)
#     if r.status_code==200:
#         soup=BeautifulSoup(r.text,'lxml')

#         # next page 
#         links = soup.find("a", class_="_9QVEpD").get('href')
#         cnp="https://www.flipkart.com"+ links
#         print(cnp)

# product_name=[]
# price=[]
# ratings=[]

# url="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove&page=2"
# r=requests.get(url)
# print(r)

# box=BeautifulSoup(r.text,'lxml')
# # box=soup.find("div",class_="DOjaWF gdgoEp")
# names=box.find_all("div",class_="KzDlHZ")
# for i in names:
#     name=i.text
#     product_name.append(name)
# print(product_name)


# prices=box.find_all("div",class_="Nx9bqj _4b5DiR")
# for i in prices:
#     prices=i.text
#     price.append(prices)
# print(price)


# rating=box.find_all("div",class_="XQDdHH")
# for i in rating:
#     rating=i.text
#     ratings.append(rating)
# print(ratings)


# # save in csv file
# extract=pd.DataFrame(
#     {
#         "name":product_name,
#         "Price":price,
#         "Ratings":ratings

#     }
# )
# # print(extract)

# extract.to_csv("Scrapped_data.csv",index=True)




# Set up Selenium WebDriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove&page=2"

# Open the URL
driver.get(url)

# Wait for the page to load
time.sleep(5)  

# Lists to store data
product_name = []
price = []
ratings = []
image=[]

name_elements = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
for name in name_elements:
    product_name.append(name.text.strip())

price_elements = driver.find_elements(By.CLASS_NAME, "Nx9bqj")
for p in price_elements:
    price.append(p.text.strip())

rating_elements = driver.find_elements(By.CLASS_NAME, "XQDdHH")
for r in rating_elements:
    ratings.append(r.text.strip() if r.text else "No rating")

image_elements = driver.find_elements(By.TAG_NAME, "img")
for img in image_elements:
    img_url = img.get_attribute("src")
    if img_url and "flipkart" in img_url:
        image.append(img_url)
# manage the length of the extracted data
max_length = max(len(product_name), len(price), len(ratings),len(image))
product_name += ["N/A"] * (max_length - len(product_name))
price += ["N/A"] * (max_length - len(price))
ratings += ["No rating"] * (max_length - len(ratings))
image += ["No Image"] * (max_length - len(image))


# Store in DataFrame
df = pd.DataFrame({
    "Product Name": product_name,
    "Price": price,
    "Ratings": ratings,
    "Image Url":image
})
# print(df)

# Save to CSV
df.to_csv("flipkart_products.csv", index=True)
print("Data saved to flipkart_products.csv")

# Close browser
driver.quit()


