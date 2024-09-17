x = 0
y = 0
z = 0

operation = input("Hello! Welcome to my calculator. Press a for addition, m for multiplication,"
      "s for subtraction, and d for division. ")

if operation == 'a':
    x =input("Please type the first number: ")
    y = input("please type the second number: ")

    z = int(x)+int(y)
    print("your answer is " + str(z))
elif operation == 'm':
    x =input("Please type the first number: ")
    y = input("please type the second number: ")

    z = int(x) * int(y)
    print("your answer is " + str(z))
elif operation == 's':
    x =input("Please type the first number: ")
    y = input("please type the second number: ")

    z = int(x) - int(y)
    print("your answer is " + str(z))
elif operation == 'd':
    x =input("Please type the first number: ")
    y = input("please type the second number: ")

    z = int(x) / int(y)
    print("your answer is " + str(z))
else:
    print("You didn't choose a letter from the list above.")


