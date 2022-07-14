alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#main function which will control the ceaser cypher program
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
        if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
   
  print(f"Here's the {cipher_direction}d result: {end_text}")
#printing the head art
from art import logo
print(logo)
#control of what to perform 'encode' or 'decode', and the main text to perform the function
loop = True
while loop:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
#if the shift is more than the number of alphabets present
  shift = shift % 25
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#enquiring weather to continue or stop the operations
  perm = input("Would you like to continue with the cipher?\nEnter 'yes' or 'no': ")
  if perm == "yes":
    loop = True
  elif perm == "no":
    loop = False
print("Goodbye!")
