# # Generate a new secret key
# import os
# from django.core.management.utils import get_random_secret_key

# # Get a new secret key
# new_secret_key = get_random_secret_key()

# # Store the new secret key as a Replit secret
# os.environ['SECRET_KEY'] = new_secret_key
# print(new_secret_key)
# print(os.environ['SECRET_KEY'])

import os

# Print all keys and their values in the environment
for key, value in os.environ.items():
    print(f'{key}: {value}')
