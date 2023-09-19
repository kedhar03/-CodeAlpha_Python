import random
import string

def generate_password(length=12):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(special_characters)]

    # Fill the remaining characters with random choices from all sets
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password characters to make it random
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

# Generate a 16-character password (you can customize the length)
generated_password = generate_password(16)
print("Generated Password:", generated_password)
