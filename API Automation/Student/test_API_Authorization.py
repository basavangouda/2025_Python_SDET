import jsonpath
import requests
from requests.auth import HTTPBasicAuth

#Base URL
base_url="https://postman-echo.com"

#Auth token
auth_token="Basic cG9zdG1hbjpwYXNzd29yZA=="

#Example 1
#approach 1
def test_basic_Authentication():
    url=base_url+"/basic-auth"
    print(url)
    header={"Authorization":auth_token}
    response=requests.get(url,headers=header)
    print(response.text)


#approach 2
def test_basic_Authentication1():
    url = base_url + "/basic-auth"
    print(url)
    response=requests.get(url,auth=HTTPBasicAuth("postman","password"))
    print(response.text)

#Example 2
#Step 1
#Here we will get authorization denied
def test_oauth_authorization_api():
    APP_URL="https://thetestingworldapi.com/api/StDetails/1104"
    response=requests.get(APP_URL)
    print(response.text)

#Step 2
#Here we will generate autorization tocken and get access
def test_oauth_authorization1_api():
    token_url="https://thetestingworldapi.com/Token"
    data={"grant_type":"password",'username':'admin','password':'adminpass'}
    response=requests.post(token_url,data)
    print(response.text)
    token_value=jsonpath.jsonpath(response.json(),"access_token")

    auth={'Authorization':'Bearer'+token_value[0]}
    APP_URL="https://thetestingworldapi.com/api/StDetails/10522573"
    response=requests.get(APP_URL,headers=auth)
    print(response.text)

