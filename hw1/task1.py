# Vigenère cipher encoder
plaintext = input("Enter plaintext:")
cipherkey = input("Enter cipher key:")
ciphertext = ''
# Uppercase A-Z => 65-90 in ASCII
# lowercase a-z => 97-122 in ASCII

ct=0 # Keep ct of num of pt chars processed, & reset once it goes past the len of ck
for char in plaintext:
    if(char.isalpha()):
        # Apply cipher key to alphabet letters
        ascii = ord(char)
        key = ord(cipherkey[ct])-65
        # print('key:'+ str(key))

        if(char.isupper()):
            #handle wrap around
            ascii= (ascii-65+key)%26+65
        elif(char.islower()):
            ascii= (ascii-97+key)%26+97

        ciphertext = ciphertext + chr(ascii)
        ct+=1
        if ct>=len(cipherkey):
            ct=0
    else:
        ciphertext = ciphertext + char

print(ciphertext)