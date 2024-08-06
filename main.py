# Imports
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import os
import time
import csv

# Clear Terminal
os.system("cls" if os.name == "nt" else "clear")

while True:
    print(f"{Fore.RED}{Style.BRIGHT}Arnis' Study Helper{Style.RESET_ALL}")
    print(
        f"What would you like to access?\n{Fore.GREEN}[1] Flashcards{Style.RESET_ALL}"
    )
    first_choice = input("")
    if first_choice == "1":
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"What would you like to do?\n{Fore.GREEN}[1] Create New Flashcard Set\n[2] Access Flashcard Set\n[3] Go Back{Style.RESET_ALL}"
            )
            second_choice = input("")
            if second_choice == "1":
                os.system("cls" if os.name == "nt" else "clear")
                # CREATE FLASHCARDS
                duplicate_checker = []
                for i in os.listdir():
                    if i.endswith(".csv"):
                        duplicate_checker.append(i)
                while True:
                    duplicate_condition = False
                    flashcard_name = input(
                        "Please enter a name for the flashcard set: "
                    )
                    for i in duplicate_checker:
                        if flashcard_name + ".csv" == i:
                            duplicate_condition = True
                            print(
                                f"{Fore.RED}ERROR: This name is already being used{Style.RESET_ALL}"
                            )
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                    if duplicate_condition == False:
                        break
                with open(f"{flashcard_name}.csv", mode="w") as flashcards:
                    flashcard_writer = csv.writer(
                        flashcards,
                        delimiter=",",
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL,
                    )
                    while True:
                        print(
                            f"Please enter the{Style.BRIGHT} front {Style.RESET_ALL}of the card"
                        )
                        front_card = input("")
                        while True:
                            print("Confirm that this is correct")
                            print(f"'{Fore.GREEN}{front_card}{Style.RESET_ALL}'")
                            confirm_front_card = input("[Y/N]")
                            if confirm_front_card.lower() == "y":
                                break
                            elif confirm_front_card.lower() == "n":
                                os.system("cls" if os.name == "nt" else "clear")
                            else:
                                os.system("cls" if os.name == "nt" else "clear")
                                print(f"{Fore.RED}Invalid Input{Style.RESET_ALL}")
                                time.sleep(1)
                                os.system("cls" if os.name == "nt" else "clear")
                        if (
                            confirm_front_card.lower() == "y"
                            or confirm_front_card.lower() == "n"
                        ):
                            break
                    while True:
                        print(
                            f"Please enter the{Style.BRIGHT} back {Style.RESET_ALL}of the card"
                        )
                        back_card = input("")
                        while True:
                            print("Confirm that this is correct")
                            print(f"'{Fore.GREEN}{back_card}{Style.RESET_ALL}'")
                            confirm_back_card = input("[Y/N]")
                            if confirm_back_card.lower() == "y":
                                break
                            elif confirm_back_card.lower() == "n":
                                os.system("cls" if os.name == "nt" else "clear")
                            else:
                                os.system("cls" if os.name == "nt" else "clear")
                                print(f"{Fore.RED}Invalid Input{Style.RESET_ALL}")
                                time.sleep(1)
                                os.system("cls" if os.name == "nt" else "clear")
                        if (
                            confirm_back_card.lower() == "y"
                            or confirm_back_card.lower() == "n"
                        ):
                            break
                    flashcard_writer.writerow([front_card, back_card])
                    flashcard_writer
            elif second_choice == "2":
                os.system("cls" if os.name == "nt" else "clear")
                # ACCESS FLASHCARDS
            elif second_choice == "3":
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{Fore.RED}ERROR: Invalid input, try again{Style.RESET_ALL}")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Fore.RED}ERROR: Invalid input, try again{Style.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
