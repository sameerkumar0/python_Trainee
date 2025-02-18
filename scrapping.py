from bs4 import BeautifulSoup
import requests
import pandas as pd
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

product_name=[]
price=[]
ratings=[]

url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=28b62c9d-1a5f-458f-b337-126ea2011cdd&as-backfill=on&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&page=4"
r=requests.get(url)
print(r)
soup=BeautifulSoup(r.text,'lxml')
names=soup.find_all("div",class_="KzDlHZ")
for i in names:
    name=i.text
    product_name.append(name)
print(product_name)


prices=soup.find_all("div",class_="Nx9bqj _4b5DiR")
for i in prices:
    prices=i.text
    price.append(prices)
print(price)


rating=soup.find_all("div",class_="XQDdHH")
for i in rating:
    rating=i.text
    ratings.append(rating)
print(ratings)


# save in csv file
extract=pd.DataFrame(
    {
        "name":product_name,
        "Price":price,
        "Ratings":ratings

    }
)
# print(extract)

extract.to_csv("Scrapped_data.csv",index=True)