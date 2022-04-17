#!/usr/bin/python3
#Validate security of accounts in a txt file

import sys
import os.path
import requests
import config


def validate_Email_File() :
    print("TEST")

def main():

    apiKey = config.api_key

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
        accountToTest = f.readline()
        requestURL = "https://haveibeenpwned.com/api/v2/breachedaccount/"
        requestStringWithAccount = requestURL + accountToTest

        response =requests.get(requestStringWithAccount)
        print(response)


main()