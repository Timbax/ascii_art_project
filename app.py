#from colorama import Fore
import pyfiglet
new_word = input("Entera word: ")

ascii_art = pyfiglet.figlet_format(new_word, font="slant")
#print(Fore.RED + font)
print(ascii_art)