# --------- BLACK JACK ---------- #
# --------- ver. 1.0 alpha -------#
#
import json
import random
import os.path

# --- configuration JSON ---

# filename = "black_jack/settings.txt"
# check_settings = os.path.exists('setting.txt')
# my_file = open(filename, 'w')

# --- ---

connect = True
check = True

while connect == True:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    total_cards = random.sample(deck, 2)
    sum_cards = sum(total_cards)
    print("Вы вытянули из колоды : " + str(total_cards) + " Сумма карт: " + str(sum_cards))
    while check == True:
        if sum_cards < 21:
            choice = input("Взять карту? (y/n): ")
            if choice == "y":
                sum_cards = sum_cards + random.choice(deck)
                print("Сумма карт: " + str(sum_cards))
            elif choice == "n":
                exit("Game over")
        elif sum_cards == 21:
            choice = input("Поздравляем, вы сорвали банк! Продолжить? (y/n)")
            if choice == "y":
                break
            elif choice == "n":
                exit("Game over")
        elif sum_cards > 21:
            choice = input("Вы проиграли банк! Продолжить? (y/n)")
            if choice == "y":
                break
            elif choice == "n":
                exit("Game over")



