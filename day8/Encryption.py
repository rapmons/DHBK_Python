


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("type 'encode' to encrypt,type 'decode' to decrypt:\n")
text=input("type your message:\n").lower()
shift= int(input("type the shift number:\n"))

def enctypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_positon=position+shift_amount
        new_letter=alphabet[new_positon]
        cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")
enctypt(text,shift)