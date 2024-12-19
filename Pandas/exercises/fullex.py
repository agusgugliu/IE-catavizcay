import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

menu = [
    '[1]. Pre-process to dataframe.',
    '[2]. Get debt information for a country and date.',
    '[3]. Get debt by type and date.',
    '[4]. Plot pie chart with internal and external debt of a country on a date.',
    '[5]. Plot bar chart with the amounts of the different types of debts of a country on a date.',
    '[6]. Plot line chart showing the evolution of a type of debt for a list of countries.',
    '[7]. Plot line chart showing the evolution of a list of debt types for a country.',
    '[8]. Plot box plot of debt by countries and types.',
    '[9]. Exit.'
]

nbr_options = menu.__len__()

asks_country = [2, 4, 5, 7]
asks_date = [2, 3, 4, 5]
asks_countrylist = [6, 8]
asks_debttype = [6]
ask_debtlist = [7, 8]

for option in menu:
    print(f'\t- {option.strip()}')

ex_repeat = True
option = 0


#Read the GDP.csv and debt.csv files into a DataFrame
gdp_csv = './files/GDP.csv'
debt = './files/debt.csv'

gdp = pd.read_csv(gdp_csv)
debt = pd.read_csv(debt)

debt.columns




while ex_repeat:
    option = int(input('Enter an option:\t').strip())

    if option == 9:
        ex_repeat = False

    if option in asks_country:
        country = input('\tEnter a country:\t').strip()
    if option in asks_date:
        date = input('\tEnter a date:\t').strip()
    if option in asks_countrylist:
        countries = []
        add_new = True        
        
        while add_new:
            country = input('\tEnter a country:\t').strip()
            countries.append(country)
            add_new = input('\tAdd another country? (y/n):\t').strip().lower() == 'y'

    if option in asks_debttype:
        debt_type = input('\tEnter a debt type:\t').strip()

    if option in ask_debtlist:
        debt_list = []
        add_new = True

        while add_new:
            debt_type = input('\tEnter a debt type:\t').strip()
            debt_list.append(debt_type)
            add_new = input('\tAdd another debt type? (y/n):\t').strip().lower() == 'y'




    if option == 1:
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

        df_long['Debt_Amount'] = pd.to_numeric(df_long['Debt_Amount'], errors='coerce')#.fillna(0)
        df_long['Date'] = df_long['YYYY']
        df_long.drop(columns=['YYYYQQ', 'YYYY'], inplace=True)

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


    
    if option == 2:
        '''
        [2] Create a function that receives a country and a date and returns a dictionary with the total internal, external, local currency, foreign currency, short term and long term debt of that country on that date.
        '''
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



    if option == 3:
        '''
        [3] Create a function that receives a type of debt and a date, and returns a dictionary with the debt of that type for all countries on that date.
        '''
        def get_debt_by_typeanddate(df, debt_type, date):
            df_filtered = df[(df['Series Name'].str.lower().str.contains(debt_type, case=False)) & (df['Date'] == date)]

            debt_by_country = df_filtered.set_index('Country Name')['Debt_Amount'].to_dict()
            
            return debt_by_country


        #EXAMPLE
        df = df_long
        debt_type = 'external'
        total = 0.0

        result = get_debt_by_typeanddate(df, debt_type, date)
        print(f'\t**{debt_type.upper()} DEBT IN {date}**')
        for key, value in result.items():
            if value > 0:
                print(f'\t\t- {key}:\t${value}.-')
                total += value

        print(f'\t\tTOTAL:\t${total}.-')



    if option == 4:
        '''
        [4] Create a function that receives a country and a date and draws a pie chart with the internal debt and external debt of that country on that date.
        '''
        def plot_debt_pie_chart(df, country, date):
            df_filtered = df[(df['Country Name'] == country) & (df['Date'] == date)]
            
            internal_debt = df_filtered[df_filtered['Series Name'].str.lower().str.contains('internal', case=False)]['Debt_Amount'].sum()
            external_debt = df_filtered[df_filtered['Series Name'].str.lower().str.contains('external', case=False)]['Debt_Amount'].sum()

            if pd.isna(internal_debt):
                internal_debt = 0
            if pd.isna(external_debt):
                external_debt = 0

            labels = ['Internal', 'External']
            values = [internal_debt, external_debt]

            if sum(values) == 0:
                print(f"No debt data available for {country} in {date}.")
                return

            plt.figure(figsize=(8, 8))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'orange'])
            plt.title(f'DEBT FOR {country.upper()} IN {date}')
            plt.axis('equal')
            plt.show()


        #EXAMPLE
        df = df_long

        plot_debt_pie_chart(df, country, date)



    if option == 5:
        '''
        [5] Create a function that receives a country and a date, and draws a bar chart with the amounts of the different types of debts of that country on that date.
        '''
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



    if option == 6:
        '''
        [6] Create a function that receives a list of countries and a type of debt and draws a line chart showing the evolution of that type of debt for those countries (one line per country).
        '''       
        def plot_debt_evolution_by_country(df,countries,debt_type):
            plt.figure(figsize=(12,8))
        
            for country in countries:
                df_filtered = df[(df['Country Name'] == country) & (df['Series Name'].str.lower().str.contains(debt_type.lower(), case=False))]

                if df_filtered.empty:
                    continue
            
                df_filtered = df_filtered.sort_values(by='Date')
                plt.plot(df_filtered['Date'],df_filtered['Debt_Amount'],label=country)

            plt.xlabel('DATE')
            plt.ylabel('DEBT')
            plt.title(f'DEBT EVOLUTION FOR {debt_type.capitalize()}')
            plt.xticks(rotation=45)
            plt.legend(title='COUNTRY')
            plt.yscale('log')
            plt.tight_layout()
            plt.show()         

        
        #EXAMPLE
        df = df_long
        plot_debt_evolution_by_country(df,countries,debt_type)



    if option == 7:
        '''
        [7] Create a function that receives a country and a list of debt types and draws a line chart showing the evolution of those debt types for that country (one line per debt type).
        '''
        def plot_type_evolution_by_country(df,country,debt_list):
            plt.figure(figsize=(12, 8))
    
            for debt_type in debt_list:
                df_filtered = df[(df['Country Name'] == country) & (df['Series Name'].str.contains(debt_type, case=False))]
                
                if df_filtered.empty:
                    continue
                df_filtered = df_filtered.sort_values(by='Date')
                
                plt.plot(df_filtered['Date'], df_filtered['Debt_Amount'], label=debt_type.capitalize())
            
            plt.xlabel('DATE')
            plt.ylabel('DEBT')
            plt.title(f'DEBT TYPE EVOLUTION BY {country.upper()}')
            plt.xticks(rotation=45)
            plt.legend(title='TYPE')
            plt.yscale('log')
            plt.tight_layout()
            plt.show()


        #EXAMPLE
        df = df_long
        plot_type_evolution_by_country(df,country,debt_list)



    if option == 8:
        '''
        [8] Create a function that receives a list of countries and a list of types of debt, and draw a box plot of debt.
        '''
        def plot_debt_by_countries_and_types(df,countries,debt_list):
            df_filtered = df[df['Country Name'].isin(countries) & df['Series Name'].str.contains('|'.join(debt_list), case=False)]
            
            df_melted = df_filtered.melt(id_vars=['Country Name', 'Date', 'Series Name'], 
                                        value_vars=['Debt_Amount'], 
                                        var_name='Debt Type', 
                                        value_name='Amount')
            
            plt.figure(figsize=(12, 8))
            sns.boxplot(x='Debt Type', y='Amount', hue='Country Name', data=df_melted, palette='Set2')
            plt.yscale('log')
            plt.title(f'DEBT DISTRIBUTION BY COUNTRIES AND TYPES')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()


        #EXAMPLE
        df = df_long
        plot_debt_by_countries_and_types(df,countries,debt_list)