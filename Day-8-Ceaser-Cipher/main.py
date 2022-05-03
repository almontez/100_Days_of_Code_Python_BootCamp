from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    message = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == 'encode':
                position = (index + shift) % len(alphabet)
            elif direction == 'decode':
                if (index - shift) < 0:
                    position = index - (shift % len(alphabet))
                else:
                    position = index - shift
            message += alphabet[position]
        else: 
            message += char
    print(f"\nThe {direction}d text is:\n{message}")

print(logo)

should_continue = True

while should_continue: 
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar(direction = direction, text = text, shift = shift)

    print("\nWould you like to continue?") 
    restart= input("Type 'yes' or 'no'. ").lower()
    if restart == "no":
        should_continue = False
        print("\nThank you for using Ceaser Cipher. Goodbye.")