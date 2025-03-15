import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Request
response = requests.get(url)

print(response)
# Display Respose Content
print(response.content)

# Validate Status code/Response Code
# Valid
assert response.status_code == 200
# Invalid
# assert response.status_code==201

# Fetch Response Header
print(response.headers)
# Fetch specific Response Header Content
print(response.headers.get('Content-Type'))
print(response.headers.get('Date'))
print(response.headers.get('Age'))
print(response.headers.get('Server'))
# Fetch Cookies
print(response.cookies)
# Fetch Encoding
print(response.encoding)
# Fetch Elapsed time
print(response.elapsed)

# If we use assertion it's called validation
assert response.encoding == "utf-8"


# Fetch the response content with Json path
import json
import jsonpath

# Send Request
response = requests.get(url)

#Parse Response to JSON format
json_response=json.loads(response.text)
print(json_response)

#Fetch the value using JSON Path
pages=jsonpath.jsonpath(json_response,'total_pages')
print(type(pages))
print(pages[0])

#Advance Json Path
first_name=jsonpath.jsonpath(json_response,'data[0].first_name')
print(first_name) #it always return list
print(first_name[0]) #it will return first element in the list
print("*********email *******************")
email=jsonpath.jsonpath(json_response,'data[0].email')
print(email[0])
print("***********for loop to get all last name*****************")
for i in range(0,4):
    last_name=jsonpath.jsonpath(json_response,"data["+str(i)+"].last_name")
    print(last_name[0])