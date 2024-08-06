# Imports
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import os
import time

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
