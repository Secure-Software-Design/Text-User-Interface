#!/usr/bin/env python
import os
import requests
import json

user_is_logged_in = False

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


def matchs_request():
    url = "http://localhost:8000/api/matchs"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def matchs_function():
    if user_is_logged_in == False:
        print("You have to log in first")
        return

    commands = ["final", "third_place", "semi_final", "quarter_final", "round_of_16", "first_stage"] 
    print("Results available : \n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format(commands[0], commands[1], commands[2], commands[3], commands[4], commands[5]))
    command_wanted = ""

    while (command_wanted == ""):
        data = input("$ ")
        if len(data) > 20:
            print("try again or exit")
        if data == "exit":
            break
        for command in commands :
            if data == command:
                command_wanted = command
                break

    data = matchs_request()
    try:
        a = json.loads(data)
        for match in a[command_wanted]:
            print(match["team1"], " VS ", match["team2"], "\t Score : ", match["goal_team1"], ':', match["goal_team2"], match["date_time"])
    except:
        print("Internal error")


def login_function():
    username = input("For login I'll need your username : ")
    password = input("And your password : ")
    resp = login_request(username, password)

    try:
        a = json.loads(resp)
        print("Logged In as ", username)
        global user_is_logged_in
        user_is_logged_in = True
    except:
        print("Bad credentials, try again")



def register_function():
    username = input("For register I'll need your username : ")
    password = input("A safe password, length from 5 -> 20 : ")
    email = input("And a good formated email : ")

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
    elif input == "match":
        return matchs_function()
    elif input == "exit":
        print("Thanks for your time, see you soon")
        os._exit(0)
    else :
        print("Unknown")


def main():
    print("Welcome to the Text User Interface of our Project\n\n Commands available:\n\tlogin\n\tregister\n\tmatch \n\t")

    while (1):
        switch(input("$ "))



if __name__ == '__main__':
    main()
