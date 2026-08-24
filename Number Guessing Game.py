import random

print("🎮 NUMBER GUESSING GAME")
print("------------------------")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < number:
        print("📉 Too Low! Try again.")
    elif guess > number:
        print("📈 Too High! Try again.")
    else:
        print("🎉 Correct!")
        print("You guessed it in", attempts, "attempts.")
        break