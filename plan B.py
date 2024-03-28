import random
import string
import os

def generate_unique_booking_reference(file_path):

    # Define the characters that can be used in the booking reference
    characters = string.ascii_uppercase + string.digits

    # Load existing references from the file if it exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_references = set(f.read().strip().splitlines())
    else:
        existing_references = set()

    # Generate a unique reference
    while True:
        reference = ''.join(random.choices(characters, k=8))#creat the reference
        if reference not in existing_references:
            # Append the new unique reference to the file
            with open(file_path, 'a') as f:
                f.write(reference + '\n')
            return reference

# run the code
file_path = 'planb booking reference.txt' #path of file
new_reference = generate_unique_booking_reference(file_path)
print(new_reference)#run
