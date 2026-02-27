import random

print("Welcome to the Guessing Number Game!")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print("Good job! You guessed my number!")
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
        
    attempts = attempts - 1
    
    if attempts > 0 and guess != secret_number:
        print("Attempts left:", attempts)

if guess != secret_number:
    print("Game over. The number I was thinking of was", secret_number)