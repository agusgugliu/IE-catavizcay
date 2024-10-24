'''
EXERCISE N°8
Write a program that manages the outstanding invoices of a company. The invoices will be stored in a dictionary where the key of each invoice will be the invoice number and the value will be the invoice cost. The program must ask the user if he wants to add a new invoice, pay an existing one or terminate. If you want to add a new invoice you will be asked for the invoice number and its cost and it will be added to the dictionary. If an invoice is to be paid, the user will be asked for the invoice number and it will be removed from the dictionary. After each operation the program should display on the screen the amount collected so far and the amount still to be collected.
'''
'''
invoices = {}
options = {
    'A': 'Add a new invoice',
    'P': 'Pay an existing invoice',
    'T': 'Terminate'
}
selected_option = ''
pending = 0
collected = 0


print("OPTIONS:")
for o in options:
    print(f"\t{o}: {options[o].upper()}")
print('----------------------------------')

while selected_option != 'T':
    selected_option = input("Select an option: ").upper()
    
    while selected_option not in options:
        print("Invalid option")
        selected_option = input("Select an option: ").upper()

    if selected_option == 'A':
        invoice_number = input("Enter the invoice number:\t")
        invoice_cost = float(input("Enter the invoice cost:\t"))
        invoices[invoice_number] = invoice_cost
        pending += invoice_cost

    if selected_option == 'P':
        invoice_number = input("Enter the invoice number:\t")
        if invoice_number in invoices:
            del invoices[invoice_number]
            collected += invoice_cost
            pending -= invoice_cost
        else:
            print("Invoice not found")

    print(f"AMOUNT COLLECTED:\t{collected}\nAMOUNT PENDING:\t\t{pending}")
'''
invoices = {}
collected = 0
pending = 0
more = ''

while more != 'T':
   if more == 'A':
       key = input('Enter invoice number: ')
       cost = float(input('Enter the cost of the invoice: '))
       invoices[key] = cost
       pending += cost
   if more == 'P':
       key = input('Enter the number of the invoice to be paid: ')
       cost = invoices.pop(key, 0)
       collected += cost
       pending -= cost
   print('Collected:', collected)
   print('Pending collection: ', pending)
   more = input('Do you want to add a new invoice (A), pay it (P) or terminate (T)? ')