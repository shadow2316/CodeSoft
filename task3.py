import random

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+<>?"

def generate_password(length, character_set):
    password = []
    for _ in range(length):
        index = random.randint(0, len(character_set) - 1)
        password.append(character_set[index])
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        print("Select complexity level:")
        print("1 - Simple (lowercase only)")
        print("2 - Moderate (lowercase and uppercase)")
        print("3 - Complex (lowercase, uppercase, and digits)")
        print("4 - Very Complex (lowercase, uppercase, digits, and special characters)")

        complexity = int(input("Complexity Level: "))
        
        character_set = ""
        if complexity == 1:
            character_set = LOWERCASE
        elif complexity == 2:
            character_set = LOWERCASE + UPPERCASE
        elif complexity == 3:
            character_set = LOWERCASE + UPPERCASE + DIGITS
        elif complexity == 4:
            character_set = LOWERCASE + UPPERCASE + DIGITS + SPECIAL_CHARACTERS
        else:
            print("Invalid choice for complexity level.")
            return

        password = generate_password(length, character_set)
        print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
