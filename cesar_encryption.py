import string
import enchant
from enchant.checker import SpellChecker

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

op = 0
while op != 1 and op != 2:
    op = int(input("1. encrypt\n2. decrypt "))

if op == 1:
    message = input("encrypt: ")
    key = 27
    while key > 26 or key < 0:
        key = int(input("enter the key (from 0 to 26): "))
    code = ''

    for i in message:
        if i in lower:
            code += lower[(lower.index(i) + key) % 26]
        elif i in upper:
            code += upper[(upper.index(i) + key) % 26]
        else:
            code += i

    print(code)

else:
    check_words = True
    code = input("enter the encryption: ")
    checker = SpellChecker("en")
    counter = 0
    while check_words == True and counter < 27: 
        message = ''
        for i in code:
            if i in lower:
                message += lower[(lower.index(i) + counter) % 26]
            elif i in upper:
                message += upper[(upper.index(i) + counter) % 26]
            else:
                message += i

        checker.set_text(message)
        check_words = False
        for error in checker:
            check_words = True
        counter += 1 
    
    print(f"The decrypted message is:\n{message} \nThe key is {27 - counter}" if check_words == False else f"No coherent message found")
    

    
    
