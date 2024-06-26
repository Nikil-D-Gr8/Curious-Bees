import json
import requests


url = "http://localhost:8000/"


data = {
    "user_id": "test_user",
    "type": "post", 
    "content": "This is some sample content for testing",
    "id": "301f6620-2a27-48f4-a284-be74e0566680"  
}

json_data = json.dumps(data)

response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

if response.status_code == 200:
    print("Success! Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
