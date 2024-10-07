# @Mahv_Core
# 0$ worth script...
# ================> Commands <=============
#                about
#                help
#                start
#                exit


from colorama import Fore, Style
from pymsgbox import *
import os
import platform
import sys

figlet = pyfiglet.Figlet(font='standard')
texa = 'SPEECH GEN'
render = figlet.renderText(texa)
system = platform.uname()[0]
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + render)
print(Fore.LIGHTBLUE_EX + f'[?]Real fucking speech checker')
print(f'[>>]Tool by : @Mahv_core.' + Fore.RESET)
print(Fore.YELLOW + f'[!]Go to https://lingojam.com/TexttoOneLine for One line Converter.' + Fore.RESET)
print(f'-------------------------------------------')

def mains():
    if system == 'Linux':
        os.system("printf '\033]2;SpeechGentod\a'")
    elif system == 'Windows':
        os.system("title SpeechGentod")
    else:
        print(f"\nPlease, Run This Tool on Linux, Windows or MacOS!\n")
        sys.exit()

mains()

while True:
    gen = input(Fore.CYAN + Style.BRIGHT + f'type "start" to permorm checking:  ')

    if gen == "about":
        alert(text=f'Tool ini digunakan untuk preparation speech bagi yang tolol dalam membuat speech.', title=f'What is Speech gen?', button=f'hah?')
    elif gen == "help":
        print(Fore.RED + f'[!]USE start TO PERFORM CHECKING' + Fore.RESET + Style.BRIGHT)
    elif gen == "start":
        def calculate_text(text):
            words = text.split()
            num_word = len(words)
            read_speed = 90
            read_time = num_word / read_speed
            
            return read_time
        def onlong_text(text):
            wordss = text.split()
            num_wordd = len(wordss)
            read_speedd = 35
            read_timee = num_wordd / read_speedd

            return read_timee

        main = input(f'Content of the speech[PASTE AS ONE LINE]: ')
        read_times = calculate_text(main)
        read_timese = onlong_text(main)
        print(Fore.YELLOW + f"The speech will take approximately {read_times:.2f} minutes, but if its long then it will take approximately {read_timese:.2f} minutes" + Fore.RESET + Style.BRIGHT)
    elif gen == "clear":
        if os.name == 'nt':
            os.system('cls')
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + render)
            print(Fore.LIGHTBLUE_EX + f'[?]Real fucking speech checker')
            print(f'[>>]Tool by : @Mahv_core.' + Fore.RESET)
        else:
            os.system('clear')
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + render)
            print(Fore.LIGHTBLUE_EX + f'[?]Real fucking speech checker')
            print(f'[>>]Tool by : @Mahv_core.' + Fore.RESET)
    elif gen == 'exit':
        sys.exit()
    else:
        print(Fore.RED + f'[!] Invaid command : ' + gen + f' ~~~')




