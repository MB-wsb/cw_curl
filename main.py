import requests
import json
import pycurl
from io import BytesIO

def send_get_request(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue().decode('utf-8')


endpoints = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/comments/3',
    'https://jsonplaceholder.typicode.com/todos'
]

def testy_api():
    test_results = {}
    for i, endpoint in enumerate(endpoints):
        response = send_get_request(endpoint)
        data = json.loads(response)

        status_code = requests.get(endpoint).status_code
        test_passed = status_code == 200
        test_results[f"Test {i + 1}"] = test_passed

        required_keys = ['id', 'title']
        for item in data:
            for key in required_keys:
                if key not in item:
                    test_results[f"Test {i + 1}"] = False

    for test, passed in test_results.items():
        if(passed):
            print(f"{test}: PASSED")
        else:
            print(f"{test}: FAILED")

testy_api()