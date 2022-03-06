import requests 
import json

def json_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Pub start/end dates need to be added to URL. Refer to API documentation if the video is unclear. 
# https://nvd.nist.gov/developers/vulnerabilities
response = requests.get('https://services.nvd.nist.gov/rest/json/cves/1.0/?pubStartDate=2021-08-04T13:00:00:000 UTC-05:00&pubEndDate=2021-10-22T13:36:00:000 UTC-05:00&keyword=tutor+lms')

json_print(response.json())
