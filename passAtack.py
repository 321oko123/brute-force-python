from random import randint
import os
pas = input("your password: ")

keys = ["1", "2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z","q"]
res = ""
pwg = ""

for x in range(len(pas)):
    res = res+pwg
    inp = pas[x-len(pas)]
    while(pwg!=inp):
        pwg=""
        for i in range(len(inp)):
                guess = keys[randint(0,34)]
                pwg = str(guess)+str(pwg)
                print(pwg)
                print("pls wait")
                print(res)
                os.system("cls")
                break
res = res+pwg
print("the pass is "+res)
