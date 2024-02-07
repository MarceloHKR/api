import requests

response = requests.get('https://api.github.com')

print(response.status_code)

#get
response = requests.get('https://jsonplaceholder.typicode.com/posts')

print("GET", response.status_code)

#post
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    data = {'title':'foo', 'body':'bar', 'userId':1}
)

print("POST", response.status_code)

#PUT
response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    data = {'title':'foo', 'body':'bar', 'userId':1}
)

print("PUT", response.status_code)

#delete

response = requests.delete(
    'https://jsonplaceholder.typicode.com/posts/1',
)

print("DELETE", response.status_code)

#GET filmes
response = requests.get('http://www.omdbapi.com/?apikey=1ece9158&t=jumanji')

print(response.status_code)

print(response.json())

#tempo
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=492485aff3ea4b06013a377a9fec8002')

print(response.status_code)

print(response.json())

#geocode
response = requests.get('https://geocode.maps.co/search?q=address&api_key=65c416d7670a5986487780dyldad80c')

print(response.status_code)

print(response.json())




