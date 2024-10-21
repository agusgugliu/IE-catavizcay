'''
EXERCISE N°4
Write a program that asks for a date in dd/mm/yyyy format and displays the same date in the format: <month>  dd,  yyyy where <month> is the name of the month.
'''
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

date = input('Enter a date in dd/mm/yyyy format: ')
day, month, year = date.split('/')
print(f'{months[int(month)]} {day}, {year}')