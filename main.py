# import files
import data
import plotting


# get data for terrorism from url
terrorism_data_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/terrorism/eu_terrorism_fatalities_by_country.csv'
# get data for murder in 2016 from url
murder_data_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2016_prelim.csv"
# get data for gender from url
gender_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'

# read data
terrorism_data = data.read_data(terrorism_data_url)
murder_data = data.read_data(murder_data_url)
gender_data = data.read_data(gender_data_url)

# Group the data
year_column = 'iyear'
country_columns = ['Belgium', 'Denmark', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Luxembourg', 'Netherlands', 'Portugal', 'Spain', 'United Kingdom']
fatalities_column = 'Fatalities'
title = 'Terrorism Fatalities in European Union by Country and Year'
# Extract the data for the year 2007
data_year = gender_data[gender_data['year'] == 2007]

# graphs plotting
plotting.plot_line_chart(terrorism_data, year_column, country_columns, fatalities_column, title)
plotting.plot_bar_chart(murder_data, 'state', ['2015_murders', '2016_murders'], 'Murders by State in 2015 and 2016 in US', 'State', 'Number of Murders')
plotting.plot_pie_chart(data_year)
