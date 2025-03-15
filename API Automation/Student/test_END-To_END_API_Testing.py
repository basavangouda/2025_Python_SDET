import requests
import json
import jsonpath

def test_create_new_Student_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\Post_payload.json", 'r')
    request_json = json.loads(f.read())
    response = requests.post(APP_URL, request_json)
    print("**********APP Response***************")
    print(response.content)
    print(response.status_code)
    id=jsonpath.jsonpath(response.json(),"id")
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\tech_POST_payload.json", "r")
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response=requests.post(tech_api_url,request_json)
    print("**********Tech API Response***************")
    print(response.content)
    print(response.status_code)
    print(response.text)

    add_url="https://thetestingworldapi.com/api/addresses"
    f=open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\Student\\address_POST_payload.json",'r')
    request_json=json.loads(f.read())
    request_json['st_id'] = id[0]
    response=requests.post(add_url,request_json)
    print("**********Address API Response***************")
    print(response.content)
    print(response.status_code)
    print(response.text)
    response_json=json.loads(response.text)
    st=jsonpath.jsonpath(response_json,"status")
    print(st)
    print(st[0])

    final_url="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_url)
    print("**********Full details fetch API Response***************")
    print(response.content)
    print(response.status_code)