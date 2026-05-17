import random

random_number = random.randint(1, 1000)

while True:
    number = input("Enter a number: ")
    
    if not number.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue
    number = int(number)
    
    if random_number > number:
        print("the raqam more than number ! 👐🏻")
        continue
    elif random_number < number:
        print("The raqam low than number ! 🤏🏻")
        continue
    else: 
        print("Congratulations !!🎉🥳🎉🥳")
    break