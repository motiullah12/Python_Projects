import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")

characters = string.ascii_letters 

if numbers.lower() == "y":
    characters += string.digits

if symbols.lower() == "y":
    characters += "!@#$%^&*"

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)