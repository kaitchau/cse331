# Vigenère cipher decoder
# Only difference is u subtract the key instead of add like in the encoder
ciphertext = input()
cipherkey = input()
plaintext = ''
# Uppercase A-Z => 65-90 in ASCII
# lowercase a-z => 97-122 in ASCII

ct=0 # Keep ct of num of pt chars processed, & reset once it goes past the len of ck
for char in ciphertext:
    if(char.isalpha()):
        # Apply cipher key to alphabet letters
        ascii = ord(char)
        key = ord(cipherkey[ct])-65
        # print('key:'+ str(key))

        if(char.isupper()):
            #handle wrap around
            ascii= (ascii-65-key)%26+65
        elif(char.islower()):
            ascii= (ascii-97-key)%26+97

        plaintext = plaintext + chr(ascii)

        # only increment in the cipherkey for alphabet letters
        ct+=1
        if ct>=len(cipherkey):
            ct=0
    else:
        plaintext = plaintext + char

print(plaintext)