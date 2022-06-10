import requests
import json

URL = "http://127.0.0.1:8005/s/"

def get_data(id=None):
    data = {}
    if id is not None:#data
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

get_data()   


def post_data():
    data = {
        'id' : 1 , 
        'name' : 'SKY',
        'roll' : 14,
        'city' : 'unai'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

# post_data()


def update_data():
    data = {
        'id' : 16,
        'name' : 'Aankit',
        'roll' : 15,
        'city' : 'BBB'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

# update_data()    


def delete_data():
    data = {
        'id' : 16,
        
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

# delete_data() 