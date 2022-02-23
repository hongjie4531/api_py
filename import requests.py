import requests 
import json

def json_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Pub start/end dates need to be added to URL. Refer to API documentation if the video is unclear. 
# https://nvd.nist.gov/developers/vulnerabilities
response = requests.get('https://services.nvd.nist.gov/rest/json/cves/1.0/?keyword=tutor+lms')

json_print(response.json())
