import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a random password with specified length and character types."""
    # Base character set
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure the password length is positive
    if length <= 0:
        return "Password length must be greater than 0."
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to interact with the user and generate passwords."""
    print("Password Generator")
    
    # Get user inputs
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input! Length must be a number.")
        return
    
    use_uppercase = input("Do you want to Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Do you want to Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Do you want to Include symbols? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
