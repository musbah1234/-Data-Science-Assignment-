# Writ a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    # Generate a random string of six characters from uppercase letters and digits
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return random_id

print(generate_random_user_id())
