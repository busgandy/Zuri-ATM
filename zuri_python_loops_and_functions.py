# -*- coding: utf-8 -*-
"""Zuri-Python-Loops-And-Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/busgandy/Zuri-Python-Loops-And-Functions/blob/main/Zuri_Python_Loops_And_Functions.ipynb

**Zuri-Python-Loops-And-Functions**
"""

import random
from datetime import datetime

database = {1299365790: ['b', 'c', 'a', 'd'], 8472256331: ['q', 'w', 'e', 'r'],
            5722564313: ["Seyi@zuri.com", "Seyi", "Zuri", "passwordSeyi"],
            8362908627: ["mike@zuri.com", "Mike", "Zuri", "passwordMike"],
            2736482567: ["love@zuri.com", "Love", "Zuri", "passwordLove"]}


def main():
    first_user_case()


def first_user_case():
    print("===============================")
    print("WELCOME TO BUSGANDA-MFB")
    print("===============================")

    # This makes sure the user enters a number as input and treats the error as an exception
    while True:
        try:
            have_account = int(input(
                "DO YOU HAVE AN ACCOUNT WITH US? \n =============================== \n RESPOND WITH THE FOLLOWING "
                "KEYS \n =============================== \n (1). YES \n (2). NO \n")
            )

            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    # This checks if the user responds appropriately
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("===============================")
        print("YOU HAVE SELECTED AN INVALID OPTION \n")
        first_user_case()


def login():
    print("===============================")
    print("WELCOME TO BUSGANDA-MFB")
    print("===============================")
    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    # This prints the date format
    print(today)
    print("=============================== \n")
    print("PLEASE LOGIN")
    print("=============================== \n")

    while True:
        try:
            account_number_from_user = int(input("WHAT IS YOUR ACCOUNT NUMBER: \n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")
    # This checks if the user input is in the database
    if account_number_from_user in database.keys():
        password = input("WHAT IS YOUR PASSWORD: \n")
        # This checks if the user's password input is also the password of the user in the database
        if database[account_number_from_user][3] == password:
            bank_operation(database[account_number_from_user])
        else:
            print("INVALID PASSWORD, TRY AGAIN. \n")
            login()
    else:
        print(
            "===============================\n THE ACCOUNT NUMBER YOU ENTERED IS NOT REGISTERED \n "
            "=============================== ")
        login()


def register():
    print("REGISTER")
    print("===============================\n")
    email = input("WHAT IS YOUR EMAIL ADDRESS: \n")
    first_name = input("WHAT IS YOUR FIRST NAME: \n")
    last_name = input("WHAT IS YOUR LAST NAME: \n")
    password = input("WHAT IS YOUR PASSWORD: \n")

    account_number = generation_account_number()
    user_details = [first_name, last_name, email, password]
    # This parses in the user input details to the database
    database[account_number] = user_details
    # print(database)|

    print("YOUR ACCOUNT HAS BEEN CREATED!")
    print("===============================\n")
    print(f"THIS IS YOUR ACCOUNT NUMBER: {account_number} \n")
    print("===============================\n")
    print("YOU CAN LOG IN WITH YOUR DETAILS \n")

    login()


def bank_operation(user):
    print(f"WELCOME {user[0]} {user[1]}")
    print("===============================\n")
    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    print(today)
    print("===============================\n")

    while True:
        try:
            selected_option = int(input(
                "WHAT WOULD YOU LIKE TO DO? \n =============================== \nRESPOND WITH THE FOLLOWING KEYS: "
                "\n===============================\n "
                "(1). Deposit \n (2). WIthdrawal \n (3). Logout \n (4). Exit\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("INVALID OPTION SELECTED, TRY AGAIN")
        bank_operation(user)


def withdrawal_operation(user):
    while True:
        try:
            option_one = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW?\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    print("===============================\n")
    print(f"TAKE YOUR CASH: #{option_one}")
    print("===============================\n")
    print("THANK YOU FOR BANKING WITH US")

    while True:
        try:
            withdrawal_option = int(input(
                "WOULD YOU LIKE TO CONTINUE YOUR TRANSACTION OR EXIT? \n RESPOND WITH: \n (1) CONTINUE. \n (2). EXIT"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")
    if withdrawal_option == 1:
        bank_operation(user)
    else:
        exit()


# This creates the deposit function
def deposit_operation(user):
    while True:
        try:
            option_two = int(input("How much would you like to deposit?\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    print(f"You Current balance is: #{option_two}.")

    while True:
        try:
            deposit_option = int(input(
                "WOULD YOU LIKE TO CONTINUE YOUR TRANSACTION OR EXIT? \n RESPOND WITH: \n (1) CONTINUE. \n ANY NUMBER "
                "TO EXIT \n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    if deposit_option == 1:
        bank_operation(user)
    else:
        exit()


# This creates the account number generation function
def generation_account_number():
    print("===============================\n")
    print("GENERATING ACCOUNT NUMBER......")
    print("===============================\n")
    # This creates a random 10 digit numbers as the password
    return random.randrange(1111111111, 9999999999)


# This creates the logout function
def logout():
    while True:
        try:
            logout_option = int(input(
                "PRESS \n (1). TO REGISTER \n (2). TO LOGIN \n OR PRESS ANY OTHER NUMBER TO TERMINATE THE TRANSACTION "
                "\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again... \n")

    if logout_option == 1:
        register()
    elif logout_option == 2:
        login()
    else:
        exit()


# This creates the exit function
def exit():
    print("===============================")
    print("THANK YOU FOR USING BUSGANDA-MFB")
    print("=============================== \n")


if __name__ == "__main__":
    main()
