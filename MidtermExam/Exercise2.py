'''
EXERCISE N°2
Define a function that receives a list of invoices, a TIN (Tax Identification Number) and a month, and returns a dictionary with the number of invoices issued to that TIN in the indicated month and the total invoiced in that month.

The function must meet the following requirements:
    • The input parameters shall be a list of invoices, a string with a TIN and another string with the month.
    • Each invoice will be represented by a dictionary with the keys tin (customer's TIN number), month (month of invoice issue), amount (amount invoiced excluding VAT), vat (VAT percentage to be applied).
    • A list with the total of each invoice (after VAT) must be created for the specified TIN number and month using functional programming or list comprehension.
    • The function must return a dictionary with the number of invoices and the total invoiced to the VAT in the indicated month.

Example of invoice:
    {'tin': 'B12345678', 'month': 'March', 'amount':1000, 'vat': 10}
'''
#FUNCTION
def summarize_invoices(invoices, tin, month):
    num_invoices = 0
    total_invoiced = 0

    for i in invoices:
        if i['tin'] == tin and i['month'] == month:
            num_invoices += 1
            total_invoiced = total_invoiced + (i['amount'] * (1 + (i['vat'] / 100)))


    return {
        'number_of_invoices': num_invoices,
        'total_invoiced': total_invoiced
    }


#PARAMETERS
invoices = [
    {'tin': 'B12345678', 'month': 'March', 'amount': 1000, 'vat': 10},
    {'tin': 'B12345678', 'month': 'March', 'amount': 2000, 'vat': 10},
    {'tin': 'B12345678', 'month': 'April', 'amount': 1500, 'vat': 10},
    {'tin': 'C87654321', 'month': 'March', 'amount': 500, 'vat': 10},
    {'tin': 'B12345678', 'month': 'March', 'amount': 2500, 'vat': 10},
    {'tin': 'C87654321', 'month': 'April', 'amount': 700, 'vat': 10},
    {'tin': 'B12345678', 'month': 'May', 'amount': 3000, 'vat': 10},
    {'tin': 'C87654321', 'month': 'March', 'amount': 800, 'vat': 10},
    {'tin': 'B12345678', 'month': 'March', 'amount': 1200, 'vat': 10},
    {'tin': 'C87654321', 'month': 'May', 'amount': 900, 'vat': 10},
    {'tin': 'AGP', 'month': 'July', 'amount': 1000, 'vat': 10},
]
tin = 'AGP'
month = 'July'


#RESULT
result = summarize_invoices(invoices, tin, month)
print(result)  