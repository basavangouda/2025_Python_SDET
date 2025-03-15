import requests
#Creating Dictionary
params={"name":"basavanagouda","email":"techtraining@qacircle.com","number":"+91-9110737775"}

#Note this API request it will do nothing we are only sending parameters
response=requests.get("https://httpbin.org/get",params=params)
print(response.text)
