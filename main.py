#!/usr/bin/python3
#Validate security of accounts in a txt file

import sys
import os.path
import time
import json

#GUI modules
from tkinter import *

#Custom modules
import HIBP

def validate_supplied_arguments():
    if len(sys.argv) != 2 :
        print("ERROR : Enter text file containing usernames as an argument")
        sys.exit()
    
def read_email_file_contents() :
    emailListFile = sys.argv[1]
    with open(emailListFile, 'r') as f:
        amountOfEmailsToSearch = sum(1 for line in open(emailListFile) if line.rstrip())
        print("\n")
        print("------------------------------------------")
        print("Commencing search on these {} emails : ".format(amountOfEmailsToSearch))
        print("------------------------------------------")
        print(f.read())
        print("------------------------------------------")
        f.seek(0, 0)
        return f.readlines()

def start_search(): 
    validate_supplied_arguments()
    emailArray = read_email_file_contents()

    for email in emailArray:
        HIBP.HIBP_get_all_breaches_for_account(email)
        time.sleep(1.55)

def main():
    root = Tk()
    root.title('ICU')
    root.geometry("500x200")
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    apiKeyLabel = Label(root, text="API Key")
    apiKeyLabel.pack()
    apiKeyEntry = Entry(root, width=40)
    apiKeyEntry.pack()
    button = Button(root, text='Start', width=25, command=start_search)
    button.pack()
    root.mainloop()


main()
