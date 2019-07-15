import requests

request = requests.get('http://api.open-notify.org/astros.json')
print(request.status_code)

print(request.text)

request_json = request.json()

print(request_json)

print("Number of people in space:",request_json['number'])

