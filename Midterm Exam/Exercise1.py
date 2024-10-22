'''
EXERCISE N°1
The directory of a company's customers is organized in a text string like the one below, where each line contains the customer's name, email, phone number, tax ID, and the discount applied to the customer. The lines are separated with the line change character and the first line contains the names of the fields with the information contained in the directory.

    "tin;name;email;telephone;discount\n01234567L;Paul Harry; paulharry @mail.com;656343576;12.5\n71476342J;Alice Brown;alice@mail.com;692839321;8\n63823376M;Peter Williams;peter@mail.com;664888233;5.2\n98376547F;Rose Anderson;rose@mail.com;667677855;15.7"

Write a program that generates a dictionary with the information of the directory, where each element corresponds to a client and has as key its tin and as value another dictionary with the rest of the information of the client. The dictionaries with the information of each client will have as keys the names of the fields and as values the information of each client corresponding to the fields. That is to say, a dictionary like the following:
    {'01234567L': {'name': 'Paul Harry', 'email': 'paulharry@mail.com', 'telephone': '656343576', 'discount': 12.5}, '71476342J': {'name': 'Alice Brown', 'email': 'alice@mail.com', 'telephone': '692839321', 'discount': 8.0}, '63823376M': {'name': 'Peter Williams', 'email': 'peter@mail.com', 'telephone': '664888233', 'discount': 5.2}, '98376547F': {'name': 'Rose Anderson', 'email': 'rose@mail.com', 'telephone': '667677855', 'discount': 15.7}}
'''

directory = "tin;name;email;telephone;discount\n01234567L;Paul Harry; paulharry @mail.com;656343576;12.5\n71476342J;Alice Brown;alice@mail.com;692839321;8\n63823376M;Peter Williams;peter@mail.com;664888233;5.2\n98376547F;Rose Anderson;rose@mail.com;667677855;15.7"
customers = {}

directory = directory.split('\n')

for d in directory[1:]:
    d = d.split(';')
    customers[d[0]] = {'name': d[1], 'email': d[2], 'telephone': d[3], 'discount': float(d[4])}

for c in customers:
    print(f'{c}: {customers[c]}')