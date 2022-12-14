from django.test import TestCase
from django.http import JsonResponse
import json

# coverage run -m pytest
# coverage report


def switch(input):
    if input == "login":
        return 1
    elif input == "register":
        return 2
    elif input == "exit":
        print("Thanks for your time, see you soon")
        return 3
    else :
        return 4


def login_function(resp_from_req):
    username = "fake username"
    password = "fake password"
    resp = resp_from_req

    if resp.find("true") != -1:
        return 0
    
    return 1


def register_function(username, password, email, response):

    if len(username) >= 50 or len(password) < 5 or len(password) > 20 or len(email) >= 50:
        print("Bad input, retry ")
    
    resp = response
    if resp.find("true") != -1:
        return 0
    return 1


def matchs_function(logged_state, datain):
    if logged_state == False:
        print("You have to log in first")
        return 1

    commands = ["final", "third_place", "semi_final", "quarter_final", "round_of_16", "first_stage"] 
    print("Results available : \n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format(commands[0], commands[1], commands[2], commands[3], commands[4], commands[5]))
    command_wanted = ""

    while (command_wanted == ""):
        data = datain
        if len(data) > 20:
            print("try again or exit")
        if data == "exit":
            break
        for command in commands :
            if data == command:
                command_wanted = command
                break


    return 0

# Create your tests here.

def test_switch_login():
    assert switch('login') == 1

def test_switch_register():
    assert switch('register') == 2

def test_switch_exit():
    assert switch('exit') == 3

def test_switch_bad_input():
    assert switch('fekofz') == 4


def test_login_function_success():
    assert login_function("true") == 0

def test_login_function_failure():
    assert login_function("false") == 1


def test_register_function_success():
    assert register_function("Julien", "admin", "email@mail.com", "true") == 0

def test_register_function_internal_error():
    assert register_function("Julien", "admin", "email@mail.com", "false") == 1


def test_register_function_bad_username():
    assert register_function("Ju", "admin", "email@mail.com", "false") == 1


def test_register_function_bad_password():
    assert register_function("Julien", "a", "email@mail.com", "false") == 1


def test_register_function_bad_email():
    assert register_function("Julien", "admin", "mail.com", "false") == 1


def test_match_function_success():
    assert matchs_function(True, "final") == 0

def test_match_function_not_log_in():
    assert matchs_function(False, "final") == 1
