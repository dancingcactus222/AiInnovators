# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:28:53 2019

@author: Jacob
"""

import random

def main():
    print("\nWelcome to Hacking")
    print("Try to guess the password from the following list: \n")
    password = ["qwerty", "password", "111111", "12345678", "abc123"]
    idx = random.randint(0,4)
    tries = 3
    for i in range(len(password)):
        print(password[i])
    
    while tries > 0:
        guess = input("Enter your guess:\n")
        if guess == password[idx]:
            print("\n*snickers* im in")
            break
        else:
            tries = tries - 1
            print("\nWrong guess")
    if tries == 0:
        print("\nGame over!")

if __name__ == "__main__":
    main()