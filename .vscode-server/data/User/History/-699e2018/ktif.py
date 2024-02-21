# Writ a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    # Generate a random string of six characters from uppercase letters and digits
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return random_id

print(generate_random_user_id())


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    # Take user input for the number of characters
    num_characters = int(input("Enter the number of characters for each user ID: "))
    
    # Take user input for the number of IDs to be generated
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    # Generate user IDs based on user inputs
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num_characters))
        user_ids.append(user_id)
    
    return user_ids

# Example usage
generated_user_ids = user_id_gen_by_user()
print("Generated User IDs:", generated_user_ids)
