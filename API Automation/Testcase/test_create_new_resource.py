import jsonpath
import pytest
import requests
import json

@pytest.fixture()
def start_exe():
        global file
        file = open("D:\\Python SDET_Work\\2025-Batches\\API Automation\\data.json", 'r')

@pytest.mark.smoke
def test_create_new_resource(start_exe):
        url = 'https://reqres.in/api/users'
        json_input = file.read()  # read json
        request_json = json.loads(json_input)  # parsing data into json
        response = requests.post(url, request_json)
        print(response.content)
        print(response.status_code)
        assert response.status_code == 201
        print(response.headers.get('Content-Type'))
        response_json=json.loads(response.text) #response into text
        print(response_json)

        # now read ID
        id = jsonpath.jsonpath(response_json, 'id')
        print(id[0])

@pytest.mark.regression
def test_create_another_resource(start_exe):
        #URL
        url='https://reqres.in/api/users'
        json_input=file.read()  #read json
        request_json=json.loads(json_input) #parsing data into json
        response=requests.post(url,request_json)
        print(response.content)
        print(response.status_code)
        assert response.status_code==201
        print(response.headers.get('Content-Type'))
