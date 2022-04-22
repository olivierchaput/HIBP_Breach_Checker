import urllib.parse
import requests
import colors

try:
    import config
except : 
    val = input("Enter API Key : ")
    with open('config.py', 'w') as f:
        f.writelines("api_key = \"" + val + "\"")
    import config


def HIBP_get_all_breaches_for_account(accountToTest):
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + urllib.parse.quote_plus(accountToTest.strip())
    hibp_api_key = config.api_key
    payload={}
    headers = {
    'hibp-api-key': str(hibp_api_key),
    'format': 'application/json',
    'timeout': '2.5',
    'HIBP': str(hibp_api_key),
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if(response.text):
        jsonResponse = response.json()
        print(colors.color.RED + str(len(jsonResponse)) + " breachs found for : " + accountToTest.strip() + colors.color.ENDC)
        for item in jsonResponse:
            print(item["Name"])
        print("\n")
    else:
        print(colors.color.GREEN + "No breach found for : " + accountToTest.strip() + colors.color.ENDC)
        print("\n")