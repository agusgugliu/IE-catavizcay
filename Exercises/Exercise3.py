'''
EXERCISE N°3
Write a program that stores in a dictionary the prices of the fruits in the table, asks the user for a fruit, a number of kilos and displays the price of that number of kilos of fruit. If the fruit is not in the dictionary it should display a message informing about it.
    Fruit Price:
    Banana 1.35
    Apple 0.80
    Pear 0.85
    Orange 0.70
'''

fruit_prices = {
    'Banana': 1.35,
    'Apple': 0.80,
    'Pear': 0.85,
    'Orange': 0.70
}

fruit = input('Enter the fruit: ').capitalize()
kilos = float(input('Enter the number of kilos: '))

if fruit in fruit_prices:
    print(f'The price of {kilos} kilos of {fruit} is: {kilos * fruit_prices[fruit]}')
else:
    print('The fruit is not in the dictionary')