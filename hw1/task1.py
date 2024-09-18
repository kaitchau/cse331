plaintext = input("Enter plaintext:")
cipherkey = input("Enter cipher key:")

# Uppercase A-Z => 65-90 in ASCII
# lowercase a-z => 97-122 in ASCII

ct=0 # Keep ct of num of pt chars processed, & reset once it goes past the len of ck
for char in plaintext:
    print(ord(char))
    ct+=1

