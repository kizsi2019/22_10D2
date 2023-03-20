import random

def generate_random_list():
    return [random.randint(0, 25) for i in range (3)]

storage = [generate_random_list() for i in range(4)]
print("The content of the 'storage' list:")
print(storage)