import random

print("Hi this is guess game for you, you have 10 chance to guess target")

low = int(input("enter lower limit: "))
high = int(input("enter higher limit: "))
target = random.randint(low,high)
gc = 0
chance = 10

while(gc<chance):
    guess = int(input("Guess number: "))
    gc = gc+1
    
    if guess == target:
        print(f'Correct! The number is {target}. You guessed it in {gc} attempts.')
        break
    elif guess<target:
        print(f'Your guess is too low. Try a higher number.')
    elif(guess>target):
        print(f'Your guess is too high. Try a lower number.')
    elif gc >= chance and guess != target:
        print(f'Sorry! The number was {target}. Better luck next time.')
    
    