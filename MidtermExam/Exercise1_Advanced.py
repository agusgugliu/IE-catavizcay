'''
EXERCISE N°1 (Advanced Version)
You are given a text string representing a directory of a company's customers, similar to the one provided below, where each line contains a customer's name, email, phone number, tax ID, discount, and customer category (e.g.: "VIP", "Regular", "New"). The lines are separated by a newline character. and the first line contains the field names.

Example input:
    "tin;name;email;telephone;discount;category\n01234567L;Paul Harry; paulharry @mail.com;656343576;12.5;VIP\n71476342J;Alice Brown;alice@mail.com;692839321;8;Regular\n63823376M;Peter Williams;peter@mail.com;664888233;5.2;New\n98376547F;Rose Anderson;rose@mail.com;667677855;15.7;VIP"

Write a program that creates a dictionary where each key is a TIN, and its value is another dictionary containing all the customer's details.
Additionally,
    - the program should categorize the customers into sub-dictionaries based on their discount range (e.g.: 0-5%, 5-10%, 10-15%, >15%).
    - the program should also return the total number of VIP customers and their average discount.
'''

def process_customer_data(data):
    lines = data.strip().split('\n')
    fields = lines[0].split(';')
    
    customers = {}
    discount_categories = {
        '0-5%': {},
        '5-10%': {},
        '10-15%': {},
        '>15%': {}
    }
    
    vip_count = 0
    vip_total_discount = 0.0
    
    for line in lines[1:]:
        details = line.split(';')
        customer_info = dict(zip(fields, details))
        
        tin = customer_info['tin']
        discount = float(customer_info['discount'])
        
        customers[tin] = customer_info
        
        if discount <= 5:
            discount_categories['0-5%'][tin] = customer_info
        elif discount <= 10:
            discount_categories['5-10%'][tin] = customer_info
        elif discount <= 15:
            discount_categories['10-15%'][tin] = customer_info
        else:
            discount_categories['>15%'][tin] = customer_info
        
        if customer_info['category'] == 'VIP':
            vip_count += 1
            vip_total_discount += discount
    
    vip_avg_discount = vip_total_discount / vip_count if vip_count > 0 else 0
    
    return customers, discount_categories, vip_count, vip_avg_discount




data = "tin;name;email;telephone;discount;category\n01234567L;Paul Harry; paulharry @mail.com;656343576;12.5;VIP\n71476342J;Alice Brown;alice@mail.com;692839321;8;Regular\n63823376M;Peter Williams;peter@mail.com;664888233;5.2;New\n98376547F;Rose Anderson;rose@mail.com;667677855;15.7;VIP"
customers, discount_categories, vip_count, vip_avg_discount = process_customer_data(data)

print("Customers Dictionary:", customers)
print("Discount Categories:", discount_categories)
print("Total VIP Customers:", vip_count)
print("Average VIP Discount:", vip_avg_discount)