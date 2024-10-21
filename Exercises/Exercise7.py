'''
EXERCISE N°7
Write a program that creates a dictionary simulating a shopping cart. The program should ask for the item and its price and add the pair to the dictionary, until the user decides to finish. Then the shopping list and the total cost should be displayed on the screen, with the following format
Shopping list	
Item 1 Price
Item 2 Price
Item 3 Price
Total Cost
'''
repeat = True
cart = {}
total_cost = 0

while repeat:
    product = str(input("Enter the product:\t")).upper()
    price = float(input("Enter the price:\t"))
    cart[product] = price
    total_cost += price
    repeat = input("Do you want to add another product? (y/n) ").lower() == 'y'

print('SHOPPING LIST')
for item in cart:
    print(f"\t- {item} ${cart[item]}")
print(f"TOTAL COST:\t\t${total_cost}")