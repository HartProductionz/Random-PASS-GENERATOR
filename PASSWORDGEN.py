# Random Secure Password Generator 7/24/23
"""
This script will allow us to get a strong random
generated password at will
Great for on the fly when you need a temporary secure password
"""

# Import the proper Modules (Random & String)
import random
import string

# Define the password gen function. (More details in ReadME)
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test out the generator by calling back the function
# "generate_strong_password"
if __name__ == "__main__":
    password_length = 12 # you can change this value, make sure to change line 13 as well


    generate_password = generate_strong_password(password_length)
    print("Generated Password:", generate_password)

"""
It is important to note that in cases, the password you generate can include passwords
from stored databases, do your due diligence by running it through databases
to see if your generated password was leaked!
"""