import json
dict='{"A":"Arjun","Q":"QACircle","B":"Basavanagouda"}'
obj=json.loads(dict)
print(obj)
print(obj['Q'])
