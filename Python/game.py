import random

options = ("piedra", "papel","tijera")
computer_option = random.choice(options)
user_option= 1

while user_option not in options:
    user_option = input("piedra, papel o tijera: ").lower()

if user_option == computer_option:
    print("Empate!")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("piedra gana a tijera")
        print("user gano!")
    else:
        print("Papel gana a piedra")
        print("computer gano!")
elif user_option == "papel" :
    if computer_option == "piedra":
        print("user gano!")
        print("papel gana a piedra")
    else:
        print("tijera gana a papel")
        print("computer gano!")
else: # user tiene tijera
    if computer_option == "papel":
        print("tijera gana a papel")
        print("user gano!")
    else:
        print("piedra gana a tijera")
        print("computer gano!")

