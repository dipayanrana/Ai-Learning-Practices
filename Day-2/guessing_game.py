import random  

target = random.randint(1, 10)  
while True:  
    guess = int(input("Guess a number between 1-10: "))  
    if guess == target:  
        print("Correct! 🎉")  
        break  
    else:  
        print("Try again!")  