import pandas as pd

menu = [
    '[1]. Pre-process to dataframe.',
    '[2]. Get debt information for a country and date.',
    '[3]. Get debt by type and date.',
    '[4]. Plot pie chart with internal and external debt of a country on a date.',
    '[5]. Plot bar chart with the amounts of the different types of debts of a country on a date.',
    '[9]. Exit.'
]

asks_country = [2, 4, 5, 7]
asks_date = [2, 3, 4, 5]

nr_options = menu.__len__()
print(nr_options)

for option in menu:
    print(option)

option = 0
again = True

while option != 9 and option not in range(1, nr_options+1):
    option = int(input('Enter an option:\t'.strip()))

    if option in asks_country:
        country = input('Enter a country:\t'.strip())
    if option in asks_date:
        date = input('Enter a date:\t'.strip())


    #-----------------------------------------------------------
    #Read the GDP.csv and debt.csv files into a DataFrame
    gdp_csv = './files/GDP.csv'
    debt = './files/debt.csv'

    gdp = pd.read_csv(gdp_csv)
    debt = pd.read_csv(debt)

    debt.columns
    #-----------------------------------------------------------
    '''
    [1] Pre-process the public debt file to obtain a data frame with:
        - Country
        - Type of Debt
        - Date
        - Amount of Debt
    '''

    columns_to_melt = debt.columns[4:]

    df_long = debt.melt(
        id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code'],
        value_vars=columns_to_melt,
        var_name='YYYYQQ',
        value_name='Debt_Amount'
    )

    df_long['YYYY'] = df_long['YYYYQQ'].str.split('Q').str[0]

    df_long['Debt_Amount'] = pd.to_numeric(df_long['Debt_Amount'], errors='coerce')
    df_long['Date'] = df_long['YYYY']
    df_long.drop(columns=['YYYYQQ', 'YYYY'], inplace=True)

    if option == 1:
        print('\n---\nEXERCISE N°1\n---\n')
        #DataFrame information
        print('- DIMENSIONS: ', df_long.shape)
        print('- NUMBER OF ELEMENTS: ', df_long.size)
        print('- DATA TYPER: ', df_long.dtypes)
        print('- COLUMN NAMES: ', df_long.columns)
        print('- NAMES OF ROWS: ', df_long.index)
        print('- NUMBER OF COUNTRIES: ', df_long['Country Name'].nunique())
        print('- LIST OF COUNTRIES: \n', df_long['Country Name'].unique())
        print('- FIRST 10 ROWS:\n', df_long.head(10))
        print('- LAST 10 ROWS:\n', df_long.tail(10))





    '''
    [2] Create a function that receives a country and a date and returns a dictionary with the total internal, external, local currency, foreign currency, short term and long term debt of that country on that date.
    '''
    elif option == 2:
        print('\n---\nEXERCISE N°2\n---\n')

        def get_debt_info(df, country, date):
            df_filtered = df[(df['Country Name'] == country) & (df['Date'] == date)]
            
            debt_types = df_filtered['Series Name'].unique()

            debt_info = {
                'internal': 0.0,
                'external': 0.0,
                'local_currency': 0.0,
                'foreign_currency': 0.0,
                'short_term': 0.0,
                'long_term': 0.0
            }

            for debt_type in debt_types:
                if 'internal' in debt_type.lower():
                    debt_info['internal'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()
                elif 'external' in debt_type.lower():
                    debt_info['external'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()
                elif 'local currency' in debt_type.lower():
                    debt_info['local_currency'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()
                elif 'foreign currency' in debt_type.lower():
                    debt_info['foreign_currency'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()
                elif 'short term' in debt_type.lower():
                    debt_info['short_term'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()
                elif 'long term' in debt_type.lower():
                    debt_info['long_term'] += df_filtered[df_filtered['Series Name'] == debt_type]['Debt_Amount'].sum()

            return debt_info

        
        #EXAMPLE
        df = df_long

        result = get_debt_info(df, country, date)
        print(country.upper())
        for key, value in result.items():
            print(f'   - {key}: {value}')




    '''
    [3] Create a function that receives a type of debt and a date, and returns a dictionary with the debt of that type for all countries on that date.
    '''
    elif option == 3:
        print('\n---\nEXERCISE N°3\n---\n')

        def get_debt_by_typeanddate(df, debt_type, date):
            df_filtered = df[(df['Series Name'].str.lower().str.contains(debt_type, case=False)) & (df['Date'] == date)]

            debt_by_country = df_filtered.set_index('Country Name')['Debt_Amount'].to_dict()
            
            return debt_by_country


        #EXAMPLE
        df = df_long
        debt_type = 'external'
        total = 0.0

        result = get_debt_by_typeanddate(df, debt_type, date)
        print(f'{debt_type.upper()} DEBT IN {date}')
        for key, value in result.items():
            if value > 0:
                print(f'   - {key}: {value}')
                total += value

        print(f'TOTAL: {total}')





    '''
    [4] Create a function that receives a country and a date and draws a pie chart with the internal debt and external debt of that country on that date.
    '''
    elif option == 4:
        print('\n---\nEXERCISE N°4\n---\n')
        import matplotlib.pyplot as plt

        def plot_debt_pie_chart(df, country, date):
            df_filtered = df[(df['Country Name'] == country) & (df['Date'] == date)]
                
            internal_debt = df_filtered[df_filtered['Series Name'].str.lower().str.contains('internal', case=False)]['Debt_Amount'].sum()
            external_debt = df_filtered[df_filtered['Series Name'].str.lower().str.contains('external', case=False)]['Debt_Amount'].sum()

            labels = ['Internal', 'External']
            values = [internal_debt, external_debt]

            plt.pie(values, labels=labels, autopct='%1.1f%%')
            plt.title(f'{country.upper()} DEBT DISTRIBUTION ON {date}')
            plt.show()



        #EXAMPLE
        df = df_long

        plot_debt_pie_chart(df, country, date)





    '''
    [5] Create a function that receives a country and a date, and draws a bar chart with the amounts of the different types of debts of that country on that date.
    '''
    elif option == 5:
        print('\n---\nEXERCISE N°5\n---\n')

        def plot_debt_bar_chart(df, country, date):
            df_filtered = df[(df['Country Name'] == country) & (df['Date'] == date)]
            
            debt_types = ['internal', 'external', 'local currency', 'foreign currency', 'short term', 'long term']
            debt_values = {debt_type: df_filtered[df_filtered['Series Name'].str.lower().str.contains(debt_type, case=False)]['Debt_Amount'].sum() for debt_type in debt_types}

            plt.bar(debt_values.keys(), debt_values.values())
            plt.xticks(rotation=90)
            plt.title(f'{country.upper()} DEBT DISTRIBUTION ON {date}')
            plt.xlabel('Debt Types')
            plt.ylabel('Debt Amount')
            plt.show()


        #EXAMPLE
        df = df_long

        plot_debt_bar_chart(df, country, date)

    elif option == 9:
        break