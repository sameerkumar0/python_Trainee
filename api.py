import requests
# # get  request using (requests library)

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response=requests.get(url)
# print(response.status_code)
# print(response.json())



# # sending data (using POST request ,Add new data )
# url = "https://jsonplaceholder.typicode.com/posts"
# data={
#     "title": "New Post",
#     "body": "This is the content of the post",
#     "userId": 1
# }

# response=requests.post(url,json=data)

# print(response.status_code)
# print(response.json())


# # Put request( update the data)

# url="https://jsonplaceholder.typicode.com/posts/1"
# data = {
#     "title": "Updated Title",
#     "body": "Updated content",
#     "userId": 1
# }

# response=requests.put(url,json=data)

# print(response.status_code)
# print(response.json())


# # delete request

# url="https://jsonplaceholder.typicode.com/posts/1"

# resp=requests.delete(url)

# print(response.status_code)
# print(response.json())


# using api key (get weather data)
import requests

API_KEY = "dc8ba822fafa4d0bacf53141251302"  #API Key
city =input("Enter city : ")

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"City: {weather_data['location']['name']}")
    print(f"Temperature: {weather_data['current']['temp_f']} °F")
    print(f"Weather: {weather_data['current']['condition']['text']}")
else:
    print("Failed to fetch data. Error:", response.status_code, response.text)



# # jso string
# import json
# json_string='{"name":"Aman","age":23,"city":"CHD"}'


# data=json.loads(json_string)
# print(data)
# print(data['name'])

# #dictionary to json(json.dumps())
# # json to dictionary (json.loads())

from bs4 import BeautifulSoup
url="https://www.amazon.in/dp/B0DSKLSV63/ref=QAHzEditorial_en_IN_1?pf_rd_r=7W1G515Y8MSJ68RC4M6G&pf_rd_p=57b6ca42-9453-42d1-b48a-bbaf4be26442&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-10&pf_rd_t=&pf_rd_i=1389401031&th=1"
req=requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

print(soup.title)
