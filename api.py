import requests
# get  request using (requests library)

url = "https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
print(response.status_code)
print(response.json())



# sending data (using POST request ,Add new data )
url = "https://jsonplaceholder.typicode.com/posts"
data={
    "title": "New Post",
    "body": "This is the content of the post",
    "userId": 1
}

response=requests.post(url,json=data)

print(response.status_code)
print(response.json())


# Put request( update the data)

url="https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}

response=requests.put(url,json=data)

print(response.status_code)
print(response.json())


# delete request

url="https://jsonplaceholder.typicode.com/posts/1"

resp=requests.delete(url)

print(response.status_code)
print(response.json())


# using api key (get weather data)
import requests

API_KEY = "dc8ba822fafa4d0bacf53141251302"  # Your API Key
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
