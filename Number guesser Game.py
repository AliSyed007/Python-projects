import random
target = random.randint(1, 100)

while True:
    userChoice = int(input("Enter your guess : "))
    

    userChoice = int(userChoice)

    if(userChoice == target):
        print("SUCCESS : CORRECT GUESS!!")
        break

    elif(userChoice < target):
        print("Your guess is smaller try a bigger one...")
    else:
        print("Your guess is bigger try a smaller one...")


print("-----GAME OVER-----")