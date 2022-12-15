#!/usr/bin/env python
import os
import sys
import requests


def login_request(username, password):
    url = "http://127.0.0.1:8000/api/user-login"

    payload={'username': username,
    'password': password}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


def register_request(username, password, email):
    url = "http://127.0.0.1:8000/api/user/"

    payload={'username': username,
    'password': password,
    'email': email}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text



def login_function():
    username = input("For login I'll need your username : ")
    password = input("And your password : ")
    resp = login_request(username, password)

    if resp.find("true") != -1:
        print("Loged In as ", username)
    
    return resp


def register_function():
    username = input("For register I'll need your username : ")
    password = input("A safe password, length from 5 -> 20 : ")
    email = input("And a good formated email :) : ")

    if len(username) >= 50 or len(password) < 5 or len(password) > 20 or len(email) >= 50:
        print("Bad input, retry ")
    
    resp = register_request(username, password, email)
    if resp.find("true") != -1:
        print("New Account ", username, " Registered !")




def switch(input):
    if input == "login":
        login_function()
    elif input == "register":
        return register_function()
    elif input == "exit":
        print("Thanks for your time, see you soon")
        os._exit(0)
    else :
        print("Unknown")
    # elif input == "Solidity":
    #     return "You can become a Blockchain developer."
    # elif input == "Java":
    #     return "You can become a mobile app developer"


def main():
    print("Welcome to the Text User Interface of our Project\n\n Commands available:\n\tlogin\n\tregister \n\t")

    while (1):
        switch(input("$ "))



if __name__ == '__main__':
    main()
