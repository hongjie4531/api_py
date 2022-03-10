import requests
import json
import datetime

def json_print(obj):
    text = json.dumps(obj, sort_keys=False, indent=1)
    print(text)

# Pub start/end dates need to be added to URL. Refer to API documentation if the video is unclear. 
# https://nvd.nist.gov/developers/vulnerabilities

def content_info(result):
    """
    This function will print out the result of the scan, results can be 0, 1 or greater than 0. I did not put in scenario for greater than 1 result yet since I tried many inputs and have not seen any scan with greater than 2 vulnerabilities.
    Function will output the scan result.
    :param result: dict format of the site.
    :return: None
    """

    # Exception handling when key error occur. Either program need to be revise, or the input date is greater than 120 days.
    try:
        print("Scan Report")
        if result["totalResults"] == 0:
            print("No Vulnerabilities found.")

        elif result["totalResults"] == 1:
        # if result has exact one vulnerability
            scan_date = (f"{datetime.datetime.now():%Y-%m-%d}")
            published_date = result["result"]["CVE_Items"][0]["publishedDate"]
            description = result["result"]["CVE_Items"][0]["cve"]["description"]["description_data"][0]["value"]
            link = result["result"]["CVE_Items"][0]["cve"]["references"]["reference_data"][0]["url"]
            confidentiality_impact = result["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["confidentialityImpact"]
            integrity_impact = result["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["integrityImpact"]
            availability_impact = result["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["availabilityImpact"]
            impact_level = result["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["baseSeverity"]

            print("Date of Scan: {}.".format(scan_date),
                  "\nVulnerability Published Date: {}.".format(published_date),
                  "\nVulnerability Description: {}.".format(description),
                  "\nConfidentiality Impact: {}.".format(confidentiality_impact),
                  "\nIntegrity Impact: {}.".format(integrity_impact),
                  "\nAvailability Impact: {}.".format(availability_impact),
                  "\nImpact Level: {}.".format(impact_level),
                  "\nFor more information, Please see the Link below:",
                  "\n{}".format(link)
                  )
        else:
            print("More than 1 vulnerability detected, please contact administrator.")

        return None

    except KeyError:
        print("Please ensure date range is within 120 days or contact administrator.")


def main():
    #Get the Information from the website

    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/1.0/?pubStartDate=2021-06-04T13:00:00:000 UTC-05:00&pubEndDate=2021-09-05T13:36:00:000 UTC-05:00&keyword=tutor+lms')
    #json_print(response.json())
    binary_content = response.content #output bin version of the information

    content = json.loads(binary_content) # Python dict format conversion
    content_info(content)

if __name__ == '__main__':
    main()
