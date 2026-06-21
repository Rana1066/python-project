import random

secret_number = random.randint(1,10);

print(secret_number)

while True:
    guess = int(input("guess the number between 1 to 10: "))

    if(guess < secret_number):
        print("You have selected small number")
    elif(guess > secret_number):
        print("You have selected High number")
    elif(guess == secret_number):
        print("You have selected the correct number")
        break