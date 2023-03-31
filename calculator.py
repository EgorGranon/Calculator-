# code page definition that lets python know which language code was written in
# -*- coding: cp1252 -*-

import math

print("Calculator")

# creating function which will force user to select a number
def getnum():
    while True:
        # try block that will catch wrong inputs
        try:
            number = int(input("Give a number: "))
            return number
        except Exception:
            print("This input is invalid.")

# storing input from user into variable using getnum function
number_1 = getnum()
number_2 = getnum()

# while loop that will keep running until break is encountered
while True:
    # printing instructions to user
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(number1/number2)\n"
          "(6) cos(number1/number2)\n(7) Change numbers\n(8) Quit\n"
          "Current numbers:", number_1, number_2)
    user_choice = int(input("Please select something (1-6): "))
    # perfoming operations according to user choice using if statements
    if user_choice == 1:
        print("The result is:", number_1 + number_2)
    elif user_choice == 2:
        print("The result is:", number_1 - number_2)
    elif user_choice == 3:
        print("The result is:", number_1 * number_2)
    elif user_choice == 4:
        print("The result is:", number_1 / number_2)
    elif user_choice == 5:
        print("The result is:", math.sin(number_1 / number_2))
    elif user_choice == 6:
        print("the result is:", math.cos(number_1 / number_2))
    elif user_choice == 7:
        # taking new values and starting a new iteration in the loop
        number_1 = getnum()
        number_2 = getnum()
        continue
    else:
        # ending the while loop
        print("Thank you!")
        break
