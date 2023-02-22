# Caesar cipher exercise part 1 & 2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
def encrypt(text, shift):
    cypher_text = ""
    for l in text:
        letter_shift = alphabet.index(l) + shift        # getting each letter from text and adding the shift amount to it
        while letter_shift > len(alphabet) -1:         #the shift will cause some letters to be out of the alphabet list index, 
            letter_shift -= len(alphabet)           # this makes them start from the begining of the alphabet again, e.g. 'z' with shift 1 = 'a'
        
        cypher_text += alphabet[letter_shift]

    print(f"The encoded text is {cypher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decipher_text = ""
    for l in text:
        new_index = alphabet.index(l) - shift        # getting each letter from text and subtracting the shift amount to it
        while new_index < 0:                      #the shift will cause some letters to be out of the index range of the alphabet list, 
            new_index += len(alphabet)  
        
        decipher_text += alphabet[new_index]
    print(f"The decoded text is {decipher_text}")

# STEP 3: combining the encrypt and decrypt functions removing repeated code:
# def caesar (text, shift, direction):
#     new_text = ""

#     if direction == "decode":
#         shift *= -1
#     for l in text:  
#         if l not in alphabet:
#             new_text += l
#             continue

#         new_index = alphabet.index(l) + shift       # getting each letter from text and adding the shift amount to it
#         while new_index > len(alphabet) -1:       # the shift will cause some letters to be out of the index range of the alphabet list, 
#             new_index -= len(alphabet)          # this makes them start from the begining of the alphabet again, e.g. 'z' with shift 1 = 'a'
#         while new_index < 0:                      # this was my solution to handle very large shifts
#             new_index += len(alphabet)

#         new_text += alphabet[new_index]
#     print(f"The {direction}d text is {new_text}")

if (direction == "encode"):
    encrypt(shift=shift, text=text)
elif (direction == "decode"):
    decrypt(shift=shift,text=text)