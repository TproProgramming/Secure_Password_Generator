import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()-=_+[]{}|;:,.<>?'
    
    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
generated_password = generate_password()
print("Generated Password:", generated_password)
