import random

guessNo=random.randint(1,9)

#instructions
print('Guess a no. between 1 and 9. You will get 5 chances')

winState=False
guessCount=1
while guessCount<=5:
    guess=int(input("Guess a no.: "))
    
    if guess>=1 and guess<=9:
        #if won
        if guess==guessNo:
            print('Congratulations! You guessed it right! You won')
            guessCount=6
            winState=True
        #hints in guesses
        elif guessNo<7 and guess+3==guessNo:
            print('The no. is more than',guess+1)
        elif (guessNo>3 and guess-3==guessNo):
            print('The no. is less than',guess-1)
        elif guessCount<5 and (guess+1==guessNo or guess-1==guessNo):
            print('You are very close! Try again')
        elif guessCount<5 and (guess+2==guessNo or guess-2==guessNo):
            print('You are close! Try again')
        elif guessNo>2 and guessNo<8:
            print('The no. is between',guessNo-2,'and',guessNo+2)

        #incrementing only when guessed b/w 1 and 9
        guessCount+=1
    else:
        print('Guess the no. between 1 and 9.')
        
#if lost
if winState==False:
    print("You lost!\nThe no. was", guessNo)
