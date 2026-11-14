#""
import os
import sys

# LBYL - Look Before You Leap
# EAFP - Easy to ASK Forgiveness than permisson
# É mais fácil pedir perdão do que permissão


try:
   names = open("names.txt").readlines()
   # ZeroDivision Error
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)

else:
    print("Sucesso")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)


