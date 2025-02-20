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
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install()) # download and install chrome browser
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--headless")  # Run without opening Chrome


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


# flipkart data
laptop_name=[]
laptop_price=[]
Ratings=[]
Description=[]

for i in range(1,10):
    url="https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    driver.get(url)
    time.sleep(5)
    box=driver.find_element(By.CLASS_NAME,"DOjaWF")
    names=box.find_elements(By.CSS_SELECTOR,"div.KzDlHZ")
    for name in names:
        names=name.text
        laptop_name.append(names)
    print(len(laptop_name))


    prices=box.find_elements(By.CSS_SELECTOR,"div._4b5DiR")
    for price in prices:
        prices=price.text
        laptop_price.append(prices)

    print(len(laptop_price))
    
    rating=box.find_elements(By.CSS_SELECTOR,"div.XQDdHH")
    for i in rating:
        rating=i.text
        Ratings.append(rating)
    print(Ratings)

    DESC=driver.find_elements(By.CLASS_NAME,"G4BRas")
    for desc in DESC:
        DESC=desc.text
        Description.append(DESC)
    print(Description)

    max_length = max(len(laptop_name), len(laptop_price), len(rating), len(Description))


    # Extend lists with "NA" if they are empty
    laptop_name.extend(["NA"] * (max_length - len(laptop_name)))
    laptop_price.extend(["NA"] * (max_length - len(laptop_price)))
    Ratings.extend(["NA"] * (max_length - len(Ratings)))
    Description.extend(["NA"] * (max_length - len(Description)))

data=pd.DataFrame({
    
    "Laptop Name":laptop_name,
    "Price":laptop_price,
    "Ratings":Ratings,
    "Descriptions":Description
},index=range(1, len(laptop_name) + 1))
data.to_csv("laptop_data.csv",index_label="Index",index=True)
driver.quit()


# # toy data

 
driver.get("https://www.flipkart.com/all/~cs-srqvl071ka/pr?sid=all&collection-tab-name=++Indoor+Games&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkluZG9vciBUb3lzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=11.productCard.PMU_V2_5&page=1")
print("Page title:", driver.title)
 
image_name=[]
image_link=[]
rating=[]
cost=[]
 
main_box=driver.find_element(By.CLASS_NAME,"DOjaWF")
img_name=main_box.find_elements(By.CLASS_NAME,"wjcEIp")
for name in img_name:
    img_name=name.text
    image_name.append(img_name)
print(len(image_name))
 
price=main_box.find_elements(By.CLASS_NAME,"Nx9bqj")
for money in price:
    price=money.text
    cost.append(price)
print(len(cost))
 
stars=main_box.find_elements(By.CLASS_NAME,"XQDdHH")
for reviews in stars:
    stars=reviews.text
    rating.append(stars)
print(len(rating))

image_elements = main_box.find_elements(By.CLASS_NAME, "DByuf4")
for img in image_elements:
    src = img.get_attribute("src")
    if src: 
        image_link.append(src)
print(image_link)


from itertools import zip_longest
aligned_data = list(zip_longest(image_name, cost, rating, image_link, fillvalue=","))

# Unpacking into separate lists
image_name, cost, rating, image_link = map(list, zip(*aligned_data))

# max_length = max(len(image_name), len(cost), len(rating), len(image_link))

# # Extend lists with "NA" if they are empty
# image_name.extend(["NA"] * (max_length - len(image_name)))
# cost.extend(["NA"] * (max_length - len(cost)))
# rating.extend(["NA"] * (max_length - len(rating)))
# image_link.extend(["NA"] * (max_length - len(image_link)))

data=pd.DataFrame(
    {
        "Product Name":image_name,
        "Product Price":cost,
        "Product Ratings ":rating,
        "Image Link":image_link
    }
)

data.to_csv("Toys1.csv",index=True,index_label="Index")
 
 
# driver.quit()