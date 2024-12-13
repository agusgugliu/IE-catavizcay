import pandas as pd

#Read the GDP.csv and debt.csv files into a DataFrame
gdp_csv = './files/GDP.csv'
debt = './files/debt.csv'

gdp = pd.read_csv(gdp_csv)
debt = pd.read_csv(debt)

debt.columns
'''
[1] Pre-process the public debt file to obtain a data frame with:
    - Country
    - Type of Debt
    - Date
    - Amount of Debt
'''
print('\n---\nEXERCISE N°1\n---\n')

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


#Example
df = df_long
country = 'Canada'
date = '1995'

result = get_debt_info(df, country, date)
print(country.upper())
for key, value in result.items():
    print(f'   - {key}: {value}')




'''
[3] Create a function that receives a type of debt and a date, and returns a dictionary with the debt of that type for all countries on that date.
'''
print('\n---\nEXERCISE N°3\n---\n')

def get_debt_by_typeanddate(df, debt_type, date):
    df_filtered = df[(df['Series Name'].str.lower().str.contains(debt_type, case=False)) & (df['Date'] == date)]

    debt_by_country = df_filtered.set_index('Country Name')['Debt_Amount'].to_dict()
    
    return debt_by_country


#Example
df = df_long
debt_type = 'external'
date = '1995'
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



#Example
df = df_long
country = 'Georgia'
date = '2017'

plot_debt_pie_chart(df, country, date)





'''
[5] Create a function that receives a country and a date, and draws a bar chart with the amounts of the different types of debts of that country on that date.
'''
print('\n---\nEXERCISE N°5\n---\n')

def plot_debt_bar_chart(df, country, date):
    # Filter the DataFrame for the specified country and date
    df_filtered = df[(df['Country Name'] == country) & (df['Year'] == date)]
    
    # Get the unique debt types and their corresponding values
    debt_types = df_filtered['Series Name'].unique()
    debt_values = df_filtered.groupby('Series Name')['Debt_Amount'].sum()

    # Plot the bar chart
    plt.bar(debt_values.index, debt_values.values)
    plt.xticks(rotation=90)
    plt.title(f'{country.upper()} DEBT DISTRIBUTION ON {date}')
    plt.xlabel('Debt Types')
    plt.ylabel('Debt Amount')
    plt.show()


#Example
df = df_long
country = 'Albania'
date = '2017'

plot_debt_bar_chart(df, country, date)


'''
[5] Create a function that receives a country and a date, and draws a bar chart with the amounts of the different types of debts of that country on that date.

'''

print('\n---\nEXERCISE N°5\n---\n')

def plot_debt_bar_chart(df, country, date): #Create function

    # Filter the DataFrame for the specified country and date
    df_filtered = df[(df['Country Name'] == country) & (df['Date'] == date)]
    
    # Get the unique debt types and their corresponding values
    debt_types = ['internal', 'external', 'local currency', 'foreign currency', 'short term', 'long term']#Define debt types
    debt_values = {debt_type: df_filtered[df_filtered['Series Name'].str.contains(debt_type, case=False)]
     ['Debt_Amount'].sum() for debt_type in debt_types} # Gives values to the debt types
    debt_values = {k: v for k, v in debt_values.items() if v > 0} #remove values that are < 0 from graph 

    # Plot the bar chart

    # Chart design  
    plt.figure(figsize=(10, 6)) #size of graph
    bars = plt.bar(debt_values.keys(), debt_values.values(), 
                   color=['skyblue', 'orange', 'green',
                          'purple', 'pink', 'brown'])
    plt.xticks(rotation=90)
    plt.title(f'{country.upper()} DEBT DISTRIBUTION ON {date}')
    plt.xlabel('Debt Types')
    plt.ylabel('Debt Amount')
    plt.show()


#Example
df = df_long
country = 'Albania'
date = '2017'

plot_debt_bar_chart(df, country, date)

'''
[6] Create a function that receives a list of countries and a type of debt and draws a line chart showing the evolution of that type of debt for those countries (one line per country).

'''

print('\n---\nEXERCISE N°6\n---\n')


def plot_debt_evolution_line_chart(df, countries, debt_type): #Create a function
    plt.figure(figsize=(12, 8)) #Chart size
    
    for country in countries: #Loop to check if the country is in the DF
        df_filtered = df[(df['Country Name'] == country) & (df['Series Name'].str.contains(debt_type, case=False))] #Filter the DF
        
        if df_filtered.empty:
            continue
        
        df_filtered = df_filtered.sort_values(by='Date') #Sort values by Date
        
        plt.plot(df_filtered['Date'], df_filtered['Debt_Amount'], label=country) # Values for graph
    
    #Graph information

    plt.xlabel('Date')
    plt.ylabel('Debt Amount')
    plt.title(f'Debt Evolution of {debt_type.capitalize()} Debt for Selected Countries')
    plt.xticks(rotation=45)
    plt.legend(title='Country')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()


#Example
countries = ['Albania', 'Canada', 'Australia']
debt_type = 'external'
plot_debt_evolution_line_chart(df_long, countries, debt_type) #Plot graph


'''
[7] Create a function that receives a country and a list of debt types and draws a line chart showing the evolution of those debt types for that country (one line per debt type).

'''

print('\n---\nEXERCISE N°7\n---\n')

def plot_multiple_debt_types_evolution_line_chart(df, country, debt_types):#Create a function
    plt.figure(figsize=(12, 8)) #Chart size
    
    for debt_type in debt_types:#Loop to check if the country is in the DF
        df_filtered = df[(df['Country Name'] == country) & (df['Series Name'].str.contains(debt_type, case=False))]#Filter the DF
        
        if df_filtered.empty:
            continue
        df_filtered = df_filtered.sort_values(by='Date') #Sort values by Date
        
        plt.plot(df_filtered['Date'], df_filtered['Debt_Amount'], label=debt_type.capitalize())# Values for graph

    #Graph information
    plt.xlabel('Date')
    plt.ylabel('Debt Amount')
    plt.title(f'Debt Evolution for {country} - Selected Debt Types')
    plt.xticks(rotation=45)
    plt.legend(title='Debt Type')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

#Example
country = 'Albania'
debt_types = ['internal', 'external', 'foreign currency']
plot_multiple_debt_types_evolution_line_chart(df_long, country, debt_types)

