
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def code():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        join1 = []
        if direction == "decode":
            shift *= -1
        for ig in text:
            if ig not in alphabet:
                join1.append(ig)
            else:
                old_index = alphabet.index(ig)
                new_index = (old_index + shift) % len(alphabet)
                join1.append(alphabet[new_index])
        join1 = "".join(join1)
        print(f"Here's your {direction}d word: {join1}")

        question = input(
            "Type 'yes' if you want to start encrypting or decrypting or 'no' to stop\n").lower()
        if question == "yes":
            code()
    else:
        print("Invalid words")
        question = input(
            "Type 'yes' if you want to start encrypting or decrypting or 'no' to stop ").lower()
        if question == "yes":
            code()

code()





