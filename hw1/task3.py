from collections import Counter

# Break the Vigenère cipher, knowing the key length
ciphertext = input("Enter ciphertext:")
cklength = int(input("Enter ck length:"))
cipherkey = ''
plaintext = ''

alpha_only_ciphertext = ''
array = ['' for i in range(cklength)]

# numbers taken from wikipedia
expected_alpha_freq = {
    'A': 8.167,
    'B': 1.492,
    'C': 2.782,
    'D': 4.253,
    'E': 12.702,
    'F': 2.228,
    'G': 2.015,
    'H': 6.094,
    'I': 6.966,
    'J': 0.153,
    'K': 0.772,
    'L': 4.025,
    'M': 2.406,
    'N': 6.749,
    'O': 7.507,
    'P': 1.929,
    'Q': 0.095,
    'R': 5.987,
    'S': 6.327,
    'T': 9.056,
    'U': 2.758,
    'V': 0.978,
    'W': 2.360,
    'X': 0.150,
    'Y': 1.974,
    'Z': 0.074
}

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


# For each column in the array (corresponding to each key position)
for i in array:
    min_chi_sq = float('inf')
    best_shift = 0

    # Try all 26 possible shifts
    for alphashift in range(26):
        # Shift the column by alphashift
        shifted = ''.join(chr(((ord(char) - 65 - alphashift) % 26) + 65) for char in i)

        # Count letter frequencies in the shifted text
        alpha_freq = Counter(shifted)

        # Calculate chi-squared value
        chi_sq = 0
        for j in range(26):
            letter = chr(j + 65)
            expected = len(i) * (expected_alpha_freq[letter] / 100)
            observed = alpha_freq.get(letter, 0)
            if expected > 0:
                chi_sq += ((observed - expected) ** 2) / expected

        # If this shift gives a lower chi-squared value, it's a better fit
        if chi_sq < min_chi_sq:
            min_chi_sq = chi_sq
            best_shift = alphashift

    # Append the best shift (as a letter) to the cipherkey
    cipherkey += chr(best_shift + 65)

print(f"Recovered key: {cipherkey}")