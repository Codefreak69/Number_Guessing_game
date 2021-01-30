import random
randNmber = random.randint(1,100)
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
            print("you guessed number just like your PP size bro... go for higher number" )


print(f"YOu guessed in {Guess} times")

with open("highscore.txt")as f:
    highscore = int(f.read())

if Guess<highscore:
    print("You got a BIG PP ...")
    with open("highscore.txt", 'w') as f:
        f.write(str(Guess))
