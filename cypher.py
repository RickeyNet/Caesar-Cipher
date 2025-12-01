
from art import logo
print(logo)

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', "'", ':', '$', '%', '"', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

crypto_is_over = False

def caesar(original_text, shift_amount, encode_or_decode):
    if direction == "encode":
        cipher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")
    elif direction == "decode":
        plain_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            plain_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {plain_text}")
    else:
        print("You chose a forbidden encryption option, pick again.")

while not crypto_is_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    repeat = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if repeat == "no":
        crypto_is_over = True