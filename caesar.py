#print(chr(ord("y")))
#print(ord(chr(121)))
#Ascil Table

key = int(input("key: "))
plaintext = input("plaintext: ")

for char in plaintext:
    if char.isupper():
        print(chr((ord(char)- 65 + key) % 26 + 65), end="")
    elif char.islower():
        print(chr((ord(char) - 97 + key) % 26 + 97), end="")
    else:
        print(char, end="")
print("")

    
# change i to the number format
# add the key to the number format
# convert back to a character3
