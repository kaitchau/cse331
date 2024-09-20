from collections import Counter

# Break the Vigenère cipher, knowing the key length
ciphertext = input("Enter ciphertext:")
cklength = int(input("Enter ck length:"))
cipherkey = ''
plaintext = ''

alpha_only_ciphertext = ''
array = ['' for i in range(cklength)]

# numbers taken from wikipedia
expected_alpha_freq = [
    8.2,   # A
    1.5,   # B
    2.8,   # C
    4.3,   # D
    12.7,  # E
    2.2,   # F
    2.0,   # G
    6.1,   # H
    7.0,   # I
    0.15,  # J
    0.77,  # K
    4.0,   # L
    2.4,   # M
    6.7,   # N
    7.5,   # O
    1.9,   # P
    0.095, # Q
    6.0,   # R
    6.3,   # S
    9.1,   # T
    2.8,   # U
    0.98,  # V
    2.4,   # W
    0.15,  # X
    2.0,   # Y
    0.074  # Z
]

#Only consider alpha chars
for char in ciphertext:
    if (char.isalpha()):
        alpha_only_ciphertext = alpha_only_ciphertext+char.upper()

#split the ct into an array for each ck a char was associated with
ct=0
for char in alpha_only_ciphertext:
    array[ct] = array[ct]+char
    ct+=1
    if ct >=cklength:
        ct=0


# Analyze each column to find the best shift
for idx, col in enumerate(array):
    print(f"Analyzing column {idx+1}")
    the_shift = ''
    min_chi_sq = float('inf')

    for alphashift in range(26):
        shifted = ''.join(chr(((ord(char) - 65 - alphashift) % 26) + 65) for char in col)

        alpha_freq = Counter(shifted)
        
        chi_sq = 0
        length = len(col)
        for j in range(26):
            letter = chr(j + 65)
            expected = length * (expected_alpha_freq[j] / 100)
            observed = alpha_freq.get(letter, 0)
            if expected > 0:
                chi_sq += ((observed - expected) ** 2) / expected
        
        print(f"Shift: {alphashift}, Chi-squared: {chi_sq}")

        if chi_sq < min_chi_sq:
            min_chi_sq = chi_sq
            the_shift = alphashift

    cipherkey += chr(the_shift + 65)

print(f"Recovered key: {cipherkey}")


