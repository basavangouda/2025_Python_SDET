import json
import jsonpath
import requests

#URL
url='https://reqres.in/api/users/2'

#Read input JSON File
file=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\data1.json",'r')
json_input=file.read()  #read json
request_json=json.loads(json_input) #parsing data into json
print(request_json)

#Make PUT Request
response=requests.put(url,request_json)

print(response.content)
print(response.status_code)
assert response.status_code==200

#Read updatedAT
#Convert the response text into json format by parsing
response_json=json.loads(response.text)
updated_li=jsonpath.jsonpath(response_json,"updatedAt")
print(updated_li[0])
