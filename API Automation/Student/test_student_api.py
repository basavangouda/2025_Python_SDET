import requests
import json
import jsonpath

def test_add_student_data():
    global ID
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\Post_payload.json","r")
    json_request=json.loads(f.read())
    response=requests.post(API_URL,json_request)
    print(response.content)
    print("********************")
    print(response.text)
    ID=jsonpath.jsonpath(response.json(),"id")
    print(ID[0])

def test_get_the_student_data():
    #This id=10522036  coming from first create method
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(ID[0])
    response=requests.get(API_URL)
    print(response.text)
    response_json=json.loads(response.text)
    id=jsonpath.jsonpath(response_json,"data.id")
    print(id[0])


def test_update_the_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/"+str(ID[0])
    f=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\PUT_Payload1.json", "r")
    json_request=json.loads(f.read())
    response=requests.put(API_URL,json_request)
    print(response.content)
    print("********************")
    print(response.text)

def test_update1_the_student_data():
    API_URL="https://reqres.in/api/users/2"
    f=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\PUT_Payload2.json", "r")
    json_request=json.loads(f.read())
    response=requests.put(API_URL,json_request)
    print(response.content)
    print("********************")
    print(response.text)

def test_delete_student_date():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(ID[0])
    response=requests.delete(API_URL)
    print(response.content)
    print(response.status_code)

