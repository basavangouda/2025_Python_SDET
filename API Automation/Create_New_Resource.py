import json

import jsonpath
import requests

#URL
url='https://reqres.in/api/users'

#Read input JSON File
file=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\data.json",'r')
json_input=file.read()  #read json
request_json=json.loads(json_input) #parsing data into json

print(request_json)

#Make Post Request
response=requests.post(url,request_json)

print(response.content)
print(response.status_code)
assert response.status_code==201

#Fetch Header from response
print(response.headers)
print(response.headers.get('Content-Type'))
print(response.headers.get('Content-Length'))

#I want to read id which is created
#first we need to parse response into JSON format
response_json=json.loads(response.text) #response into text

print(response_json)

#now read ID
id=jsonpath.jsonpath(response_json,'id')
print(id[0])
