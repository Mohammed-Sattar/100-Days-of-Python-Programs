# Day 8 Project - Caesar Cipher:
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar (text, shift, direction):
    new_text = ""
    shift %= 26         # to handle very large shifts

    if direction == "decode":
        shift *= -1

    for l in text:  
        if l not in alphabet:
            new_text += l
            continue

        new_index = alphabet.index(l) + shift       # getting each letter from text and adding the shift amount to it
        new_text += alphabet[new_index]
    print(f"The {direction}d text is {new_text}")

repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
