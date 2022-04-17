#!/usr/bin/python3
#Validate security of accounts in a txt file

import sys
import os.path
import requests
import time
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
        print(colors.RED + "Breachs found for : " + accountToTest.strip() + colors.ENDC)
        print(response.text)
        print("\n")
    else:
        print(colors.GREEN + "No breach found for : " + accountToTest.strip() + colors.ENDC)
        print("\n")

def main(): 
    if len(sys.argv) != 2 :
        print("ERROR : Enter text file containing usernames as an argument")
        sys.exit()

    emailListFile = sys.argv[1]
    with open(emailListFile, 'r') as f:
        amountOfEmailsToSearch = sum(1 for line in open(emailListFile) if line.rstrip())
        print("------------------------------------------")
        print("Commencing search on these {} emails : ".format(amountOfEmailsToSearch))
        print("------------------------------------------")
        print(f.read())
        print("------------------------------------------")
        f.seek(0, 0)
        accounts = f.readlines()
    
    for account in accounts:
        HIBP_get_all_breaches_for_account(account)
        time.sleep(1.6)

main()