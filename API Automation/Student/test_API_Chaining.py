import requests
import json
import jsonpath

def test_create_new_Student_data():
    global ID
    URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\Post_payload.json", 'r')
    request_json = json.loads(f.read())
    response = requests.post(URL, request_json)
    print("**********API Response***************")
    print(response.content)
    print(response.status_code)
    ID=jsonpath.jsonpath(response.json(),"id")
    print(ID[0])

def test_get_student_details():
    url = "https://thetestingworldapi.com/api/studentsDetails/"+str(ID[0])
    print(url)
    response=requests.get(url)
    print(response.status_code)
    print(response.text)
    print(response.content)
    m_name=jsonpath.jsonpath(response.json(),"data.middle_name")
    print(m_name[0])
