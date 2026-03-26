import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    years = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    fig,ax = plt.subplots(figsize=(14,6))
    ax = plt.scatter(years,sea_level)

    
    # Create first line of best fit
    line1 = linregress(years, sea_level)
    x1 = np.arange(min(years), 2051)  
    y1 = line1.slope * x1 + line1.intercept
    plt.plot(x1, y1, color='red', label='Line of Best Fit')
    
    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000] 
    line2 = linregress(df2000['Year'],df2000['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051,1)
    y2 = line2.slope*x2 + line2.intercept
    plt.plot(x2,y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
