import json
import requests

url = 'http://127.0.0.1:8000/LEED_prediction'

input_data_for_model = {

    'GrossFloorArea': 647000.00,
    'State': 11,
    'OwnerTypes': 5,
    'ProjectTypes': 11

}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)