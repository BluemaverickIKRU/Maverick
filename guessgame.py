#Guessing game

secret_num = 10
chance = 0
guess_limit = 3

while chance < guess_limit:
    guess = int(input("Guess: "))
    chance += 1
    if guess == secret_num:
        print("You have Won! :)")
        break

else:
    print("You have lost the chances :(")
