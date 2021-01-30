import random
randNmber = random.randint(1,100)
# print(randNmber)
Guess = 0
userGuess = None


while(userGuess != randNmber):
    userGuess = int(input("Enter your Guess: "))
    Guess += 1
    if userGuess == randNmber:
        print("EUREKA!!!!!!!!You guessed it right!!")
    else:
        print("BRUHHH!!! You guessed the wrong number!!")
        if(userGuess>randNmber):
            print(f"Ughhhh ..you guessed pretty higher...go for lower number :)")
        elif userGuess<randNmber:
            print("you guessed your penis size bro... go for higher number" )




print(f"YOu guessed in {Guess} times")