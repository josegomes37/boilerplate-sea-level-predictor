import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    #fig, ax = plt.subplots(figsize=(20,10))
    #ax = plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')


    # Create first line of best fit
    lineg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(range(df['Year'].min(), 2050,1), lineg.slope*range(df['Year'].min(),
                                                           2050,1)+lineg.intercept)


    # Create second line of best fit
    lineg_2 = linregress(df.query('Year >= 2000')['Year'],
                    df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000,2050,1), lineg_2.slope*range(2000,2050,1)+lineg_2.intercept)
    #print(ax)
    #print(lineg_2.slope*2050+lineg_2.intercept)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()