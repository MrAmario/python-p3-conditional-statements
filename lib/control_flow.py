#!/usr/bin/env python3

def admin_login(username, password):
    if (username == ("admin" or "ADMIN")
    and password == 12345):
        print("Access granted")
    else:
        print("Access denied")

admin_login("admin", 12345)

def hows_the_weather(temperature):
    if temperature<40:
        print("It's bricks out here!")
    elif temperature > 40 or temperature < 65:
        print("It's a little chilly out here!")
    elif temperature > 85:
        print("It's too dang hot out here!")
    else:
        print("It's perfect out here!")

hows_the_weather(55)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
   

fizzbuzz(18)

def calculator(operation, num1, num2):
    if operation == "+" :
        sum = num1 + num2
        print(sum)
    elif operation == "-":
        sub = num1 - num2
        print(sub)
    elif operation == "*":
        multi = num1 * num2
        print(multi)
    elif operation == "/":
        div = num1 / num2
        print(div)
    else:
        print("None")
calculator("cow", 9, 3)
