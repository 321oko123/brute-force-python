import os
pas = input("your password: ")

keys = ["1", "2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z","q","v","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":","'",'"',",","<",".",">","/","?","|"]
res = ""
pwg = ""
y=0
for x in range(len(pas)):
    res = res+pwg
    inp = pas[x-len(pas)]
    y=0
    while(pwg!=inp):
        pwg=""
        for i in range(len(inp)):
                guess = keys[y]
                pwg = str(guess)+str(pwg)
                print(pwg)
                print("pls wait")
                print(res)
                os.system("cls")
                y=y+1
                    
res = res+pwg
print("the pass is "+res)
