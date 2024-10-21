'''
EXERCISE N°2
Write a program that asks the user for his name, age, address and telephone number and stores it in a dictionary. It should then display the message <name> is <age> years old, lives at <address> and his phone number is <phone>.
'''

user_info = {
    'name': input('Enter your name:\t\t'),
    'age': input('Enter your age:\t\t\t'),
    'address': input('Enter your address:\t\t'),
    'phone': input('Enter your phone number:\t')
}

print(f"{user_info['name']} is {user_info['age']} years old, lives at {user_info['address']} and his phone number is {user_info['phone']}.")