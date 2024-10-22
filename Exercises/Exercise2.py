'''
EXERCISE N°2
Write a program that asks the user for his name, age, address and telephone number and stores it in a dictionary. It should then display the message <name> is <age> years old, lives at <address> and his phone number is <phone>.
'''

vName = input('Enter your name:\t\t')
vAge = int(input('Enter your age:\t\t\t'))
vAddress = input('Enter your address:\t\t')
vPhone = input('Enter your phone number:\t')

user_info = {
    'name': vName,
    'age': vAge,
    'address': vAddress,
    'phone': vPhone
}

print(f"{user_info['name']} is {user_info['age']} years old, lives at {user_info['address']} and his phone number is {user_info['phone']}.")