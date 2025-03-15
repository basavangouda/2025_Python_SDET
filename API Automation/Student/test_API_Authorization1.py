import requests
import json
import random
import Random_email


#base url:
base_url='https://gorest.co.in/'

#Auth token:
auth_token='Bearer db23b9c849386ae09beb1651b2bd59cab614afdedf7a1ba886ebc3098b4f379c'

#GET Request
def test_get_request():
   url=base_url+'/public/v2/users'
   print("Get URL :-",url)
   header={"Authorization":auth_token}
   response=requests.get(url,headers=header)
   assert response.status_code==200
   print(response.text)
   print(type(response.text))
   print("***********************************")
   print(type(response.json()))
   print("*****I want output should be in Json`")
   json_str=json.dumps(response.json(),indent=4)
   print(json_str)
   print(".....GET....IS DONE")


#POST Request
def test_post_request():
   url = base_url + 'public/v2/users'
   print("POST URL :-", url)
   header = {"Authorization": auth_token}
   #Payload data create
   data={
           "name":"Basavana Gouda",
            "gender":"male",
            "email":Random_email.generate_random_email(),
            "status":"active"
       }


   response = requests.post(url,headers=header,json=data)
   print(response.json())
   print(response.status_code)
   assert response.status_code==201
   json_data=response.json()
   print(type(json_data))

   global user_id
   user_id=json_data['id']
   print(user_id)
   assert "name" in json_data
   assert json_data['name'] == "Basavana Gouda"


   print("*****I want output should be in Json`")
   json_str = json.dumps(response.json(), indent=4)
   print(json_str)
   print(".....POST....IS DONE")


#PATCH Request
def test_patch_request():
   url = base_url + f'public/v2/users/'+str(user_id)
   print("PATCH URL :-", url)
   header = {"Authorization": auth_token}


   # Payload data create
   #I want to update Name and status In-Active
   data = {"name":"Basavana Gouda QA",
           "email":Random_email.generate_random_email(),
           "status":"active"}


   response = requests.patch(url,headers=header,json=data)
   print(response.json())
   print(response.status_code)
   assert response.status_code == 200
   json_data = response.json()
   print(json_data)
   assert 'name' in json_data
   assert json_data['status']=='active'


   print("*****I want output should be in Json`")
   json_str = json.dumps(response.json(), indent=4)
   print(json_str)
   print(".....PATCH....IS DONE")


#Put Request
def test_put_request():
   url = base_url + f'public/v2/users/'+str(user_id)
   print("PUT URL :-", url)
   header = {"Authorization": auth_token}


   # Payload data create
   #I want to update Name and status In-Active
   data = {"name":"Basavana Gouda QA",
           "email":Random_email.generate_random_email(),
           "status":"active"}


   response = requests.put(url,headers=header,json=data)
   print(response.json())
   assert response.status_code==200
   json_string=response.json()
   assert json_string['id']==user_id
   assert json_string['name']=="Basavana Gouda QA"
   print(json.dumps(response.json(),indent=4))
   print(".....PUT....IS DONE")


#Delete Request
def test_delete_request():
   url = base_url + f'public/v2/users/'+str(user_id)
   print("DELETE URL :-", url)
   header = {"Authorization": auth_token}
   response = requests.delete(url,headers=header)
   assert response.status_code==204
   print(".....DELETE....IS DONE")



