import requests
# GET
# response = requests.get('https://api.github.com/events')
# print(response.json())

# POST

response = requests.post('https://httpbin.org/post', data = {'abacate': 'come abacate come'})
print(response.json())
