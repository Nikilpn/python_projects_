
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text,shift_key):#hello 
    cipher_text=""               
    for char in plain_text:   #we need to find position of alphabet in typed text
        if char in alphabet:
            position=alphabet.index(char)

            newposition=(position+shift_key)%26
            cipher_text+=alphabet[newposition]
        else:
            cipher_text+=char
    print(f"the encrypted text is: {cipher_text}")
def decryption(cipher_text,shift_key):#khoor
    plain_text=""
    for char in cipher_text:   #we need to find position of alphabet in typed text
        if char in alphabet:
            position=alphabet.index(char)

            newposition=(position-shift_key)%26
            plain_text+=alphabet[newposition]
        else:
            plain_text+=char
    print(f"the decrypted text is: {plain_text}")

                                                




wanna_end=False
while not wanna_end:
    what_to_do = input("Type encrypt for encrption,Type decrypt for decryption:\n")

    text = input("enter your text")
    shift = int(input("enter your shift key"))

    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    play_again=input("Type 'yes' to continue,Type 'no' to exit \n")
    if play_again=="yes":
        wanna_end=False
    else:
        print("Have a Nice day. Good bye!")
        wanna_end=True






