'''
EXERCISE N°1
Write a program that stores in a variable the dictionary {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, asks the user for a currency and displays its symbol or a warning message if the currency is not in the dictionary.
    currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    currency = input("Enter a currency: ")
    print(currencies.get(currency.title(), "Currency is missing."))
'''

currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input('Enter a currency:\t')

if currency.title() in currencies:
    print(currencies[currency.title()])
else:
    print('Currency is missing.')