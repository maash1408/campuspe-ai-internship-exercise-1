import requests
import json

print("="*60)
print("Working with Rest APIs")
print("="*60)

jsonolaceholder_url = "https://jsonplaceholder.typicode.com"
req_url = jsonolaceholder_url + "/posts/1"
print(req_url)

payload = {}
headers = {}
url = req_url
# response = requests.request("GET", url, headers=headers, data=payload)

# params={'userId':1}
# response = requests.get(f"{url}/posts",param=params)
# print(response)
# print(response.text)

print("\n 3. POST Request")
new_post = {
    "userId": 1,
    "title": "Testing AI Placeholder response",
    "body": "Body for Testing AI Placeholder response request"
}

postresponse = requests.post(f"{url}/posts",json=new_post)
print(postresponse)
print(postresponse.text)