import pandas as pd
import plotting

# function that reads file as argument and return two data set
def read_worldbank_data(filename):
    # read in data
    df = pd.read_csv(filename, skiprows=4)
    # transpose dataframe to create year columns
    df_year = df.set_index('Country Name').T
    # clean up column headers
    df_year.columns.name = ''
    # transpose dataframe again to create country columns
    df_country = df_year.T
    df_country.columns.name = 'Country Name'
    # clean up any NaN values
    df_year.fillna('', inplace=True)
    df_country.fillna('', inplace=True)
    # return both dataframes
    return df_year, df_country

df_year, df_country = read_worldbank_data('climatechange.csv')
# drop unnecessary columns
df_country.drop(['Unnamed: 66'], axis=1, inplace=True)

# year as column
print(df_year)

# country as column
print(df_country)

# Read in the World Bank data and create separate dataframes for years and countries
df_year, df_country = read_worldbank_data('climatechange.csv')


# Read the CSV file
df = pd.read_csv('climatechange.csv', skiprows=4)
df.drop(['Unnamed: 66'], axis=1, inplace=True)
df.fillna('', inplace=True)

# Indicators of interest
indicators = ['Total greenhouse gas emissions (kt of CO2 equivalent)', 'Urban population (% of total population)', 'Forest area (% of land area)', 'Arable land (% of land area)', 'Electric power consumption (kWh per capita)', 'CO2 emissions from liquid fuel consumption (% of total)']

# Countries of interest
countries = ['Bangladesh','Brazil','Canada','China','France','India','Nigeria','South Africa','Sweden','Switzerland','United Kingdom','United States']

# Subset the data for the chosen indicators and countries
df_sub = df[(df['Country Name'].isin(countries)) & (df['Indicator Name'].isin(indicators))]

# Calculate summary statistics for each indicator for each country using describe function
summary_stats = df_sub.groupby(['Country Name', 'Indicator Name']).describe()

# Print the summary statistics for each indicator for each country
print(summary_stats)

# Create a list of column names containing year values
year_columns = [col for col in df_sub.columns if col.isdigit()]



# Subset the data for the chosen indicators and countries
df_filterTable = df[df['Indicator Name'] == 'Urban population (% of total population)']
df_filterTable.drop(['Indicator Name'], axis=1, inplace=True)
df_filterTable = df_filterTable.set_index('Country Name')

# Create a list of column names containing year values
year_columns = [str(year) for year in range(1960, 2021)]

# Print the table
print(df_filterTable.loc[countries, '1960':'2020'])

# graphs plotting/statistical representation
plotting.plot_bar_chart(df_sub, year_columns, 'Total greenhouse gas emissions (kt of CO2 equivalent)', 'Country Name', '')
plotting.plot_bar_chart(df_sub, year_columns, 'Electric power consumption (kWh per capita)', 'Country Name', '')
plotting.plot_heatmap_chart(df_sub, 'China', indicators,'Blues')
plotting.plot_heatmap_chart(df_sub, 'United States', indicators,'YlGnBu')
plotting.plot_heatmap_chart(df_sub, 'Bangladesh', indicators,'crest')
