import random
secretNumber = random.randint(1, 20)
print("Iam thinking of a number between 1 and 20")
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    #Ask a player to guess 6 times
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job you guessed my number in' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number iwas thinking of was ' + str(secretNumber))
    
