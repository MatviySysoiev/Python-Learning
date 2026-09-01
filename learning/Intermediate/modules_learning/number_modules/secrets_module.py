import secrets
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(25)))

# print(string.ascii_letters)  # All English letter (capital and small)
# print(string.ascii_lowercase)  # All Small English letters
# print(string.ascii_uppercase)  # All Capital English letters
# print(string.digits)  # All numbers from 0 to 9
# print(string.punctuation) # all punctuation symbols
