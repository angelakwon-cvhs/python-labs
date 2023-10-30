# Question 0: Please put the code for your warmup here






# Question 1: Fill in the conditions to make the print statements run correctly.
i = input("Give me a number between 1 and 10")
if #PUT_CONDITION_HERE:
    print("i is less than 5")
else:
    if # PUT CONDITION HERE:
        print("i is less than 10")
    else:
        print("i is 10")

## PUT ANSWER HERE


# Question 2: How would we rewrite the code above using an elif statement?
## PUT ANSWER HERE

# Question 3: What is outputted?

age = 50
if age % 10 == 0:
    print("The number is divisible by 10")
if age % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 10 or 5")

## PUT ANSWER HERE


# Question 4: What is outputted?

age = 50
if age % 10 == 0:
    print("The number is divisible by 10")
elif age % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 10 or 5")

## PUT ANSWER HERE

# Question 5: The code in question 3 and the code in question 4 look similar, but behave very differently. 
# Why is that?
## PUT ANSWER HERE

# Question 6: What does this code output?
number = 5
if number % 5 == 0:
    print("The number is divisible by 5")
if number >= 5:
    print("The number is greater than or equal to 5")
## PUT ANSWER HERE

# Question 6.1: What does this code output?
number = 6
if number % 5 == 0:
    print("The number is divisible by 5")
if number >= 5:
    print("The number is greater than or equal to 5")
## PUT ANSWER HERE

# Question 6.2: What does this code output?
number = 4
if number % 5 == 0:
    print("The number is divisible by 5")
if number >= 5:
    print("The number is greater than or equal to 5")
## PUT ANSWER HERE

# Question 7: What does this code output?
number = 6
if number % 5 == 0:
    if number % 2 == 0:
        print("This number is divisible by 5 and 2")
else:
    print("This number is not divisible by 5")
print("This will print regardless")
## PUT ANSWER HERE

# Question 7.1: What does this code output?
number = 10
if number % 5 == 0:
    if number % 2 == 0:
        print("This number is divisible by 5 and 2")
else:
    print("This number is not divisible by 5")
print("This will print regardless")
## PUT ANSWER HERE

# Question 8: What does this code output?
number = 5
if number + 5 < 15:
    number = number + 5
    if number + 5 < 20:
        print(number)
else:
    print(number)
## PUT ANSWER HERE

# Question 9: What does this code output?
number = 5
if number == "5":
    print("The variable number is a string")
if number == 5:
    print("The variable number is an integer")
if str(number) == "5":
    print("Casting makes this true")
## PUT ANSWER HERE

# Question 10: Write a program that takes in a percentage between 0 and 100 from the user and prints out a corresponding letter grade.
# Hint: You will want to use elif statements here! Remember that your first statement needs to be an if statement though.