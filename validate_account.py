#!/usr/bin/python3
#Validate security of accounts in a txt file

import sys
import os.path
import requests
import time
import json
import urllib.parse

#Custom modules
try:
    import config
except : 
    val = input("Enter API Key : ")
    with open('config.py', 'w') as f:
        f.writelines("api_key = \"" + val + "\"")
    import config


class colors: 
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def get_pretty_json_string(value_dict):
    return json.dumps(value_dict, indent=4, sort_keys=True, ensure_ascii=False)


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
        print(colors.RED + str(len(jsonResponse)) + " breachs found for : " + accountToTest.strip() + colors.ENDC)
        for item in jsonResponse:
            print(item["Name"])
        print("\n")
    else:
        print(colors.GREEN + "No breach found for : " + accountToTest.strip() + colors.ENDC)
        print("\n")

def validate_supplied_arguments():
    if len(sys.argv) != 2 :
        print("ERROR : Enter text file containing usernames as an argument")
        sys.exit()
    
def read_email_file_contents() :
    emailListFile = sys.argv[1]
    with open(emailListFile, 'r') as f:
        amountOfEmailsToSearch = sum(1 for line in open(emailListFile) if line.rstrip())
        print("------------------------------------------")
        print("Commencing search on these {} emails : ".format(amountOfEmailsToSearch))
        print("------------------------------------------")
        print(f.read())
        print("------------------------------------------")
        f.seek(0, 0)
        return f.readlines()

def main(): 

    validate_supplied_arguments()
    emailArray = read_email_file_contents()

    for email in emailArray:
        HIBP_get_all_breaches_for_account(email)
        time.sleep(1.55)

main()