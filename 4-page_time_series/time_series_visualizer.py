import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',sep=',',parse_dates=['date'],index_col=0)

# Clean data
top = df['value'].quantile(0.925)
bottom = df['value'].quantile(0.025)
df = df[df['value'].between(bottom,top)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,8))
    sns.lineplot(df,x=df.index,y=df['value'],ax=ax)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019.')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    data = df.groupby(by=[df.index.year.rename('year'),df.index.month.rename('month')]).mean()
    data = data.reset_index()
    
    data['month'] = pd.to_datetime(data['month'],format='%m').dt.month_name()
    data['month'] = pd.Categorical(data['month'],categories=[
            'January','February','March','April','May','June',
            'July','August','September','October','November','December'],ordered=True)

    # Draw bar plot
    fig,ax = plt.subplots(figsize=(12,8))
    sns.barplot(data=data,x='year',y='value',hue='month',palette='Paired')
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(14,6))
    sns.boxplot(df_box,x=df_box['year'],hue=df_box['month'],palette='Set2',
                legend=False,ax=ax1)    
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Month')
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    sns.boxplot(df_box,x=df_box['month'],hue=df_box['year'],palette='Set2',
                legend=False,ax=ax2)    
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Year')
    ax2.set_title('Month-wise Box Plot (Trend)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
