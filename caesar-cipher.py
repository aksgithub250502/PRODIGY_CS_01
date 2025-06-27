# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  # Only shift letters
            # Check for uppercase
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            # Check for lowercase
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave special characters unchanged
            result += char
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Reverse the shift

# Main program
def main():
    print("Caesar Cipher Program")
    
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice! Please choose 'e' or 'd'.")

# Run the main function
main()