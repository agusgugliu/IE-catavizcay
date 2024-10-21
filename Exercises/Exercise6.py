'''
EXERCISE N°6
Write a program that creates an empty dictionary and fills it with information about a person (e.g. name, age, gender, telephone, e-mail, etc.) that is requested from the user. Each time a new piece of information is added, the contents of the dictionary must be printed.
'''
person = {}
repeat = True
while repeat:
    attribute = input('What data do you want to enter?\t')
    value = input(attribute + ': ')
    person[attribute] = value
    print(person)    
    repeat = input('Do you want to add more information (Yes/No)? ').upper() == "YES"