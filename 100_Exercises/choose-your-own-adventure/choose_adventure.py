print("You find yourself standing at a crossroads.")
print("Choose your path:")
print("1. Take the left path.")
print("2. Take the middle path.")
print("3. Take the right path.")
# Will ask the user to type an input and assign to the 'choice' variable
# All inputs are assigned as type 'string'
choice = input("Enter the number of your choice: ")
if choice == "1":
    print("You take the left path")
    # TODO: fill this out more with at least 2 more user inputs, one of which using an elif statement
elif choice == "2":
    print("You take the middle path")
    # TODO: fill this out more with at least 2 more user inputs, one of which using an elif statement
elif choice == "3":
    print("You take the right path")
    # TODO: fill this out more with at least 2 more user inputs, one of which using an elif statement
else:
    print("Invalid choice. Please enter 1, 2, or 3 next time. Exiting game")
