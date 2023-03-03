import matplotlib.pyplot as plt

def plot_line_chart(data, x_col, y_col, y_label, title):

    # Group data by year and sum the number of fatalities for each country
    group_data = data.groupby([x_col]).sum()[y_col]

    # Define the graph type and image size
    ax = group_data.plot(kind='line', figsize=(10,8))

    # Set title and axis labels
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_label)

    # Show the graph
    plt.show()

# Bar Graph
def plot_bar_chart(data, x_col, y_col, title, x_label, y_label):
    """
    Read a CSV file from the given URL, group the data by the values in the state_column,
    and create a grouped bar chart showing the values in the murder_columns for each group.
    """
    state_data = data.groupby(x_col)[y_col].sum()
    # Define the graph type and image size
    state_data.plot(kind='bar', figsize=(12,8))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()    

    
# Pie Graph
def plot_pie_chart(data):
    """
    Plot a pie chart of the mean GDP per capita by continent.
    Expects a pandas DataFrame with a 'continent' column and a 'gdpPercap' column.
    """
    continent_mean = data.groupby('continent')['gdpPercap'].mean()
    plt.pie(continent_mean.values, labels=continent_mean.index, autopct='%1.1f%%')
    plt.title(f'Mean GDP per Capita by Continent in {data["year"].iloc[0]}')
    plt.show()