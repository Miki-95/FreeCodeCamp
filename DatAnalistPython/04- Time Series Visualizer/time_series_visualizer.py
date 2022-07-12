import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime 


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Pasamos a formato fecha la fecha
df['date']= pd.to_datetime(df['date'], format="%Y-%m-%d")

df = df.set_index('date')
#df.index= pd.to_datetime(df.index, format="%Y-%m-%d")


# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) &(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    fig.set_figheight(15)
    fig.set_figwidth(30)
    df.plot(ax = ax, color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-    12/2019', fontdict = {'fontsize':50})
    ax.set_ylabel('Date', fontdict = {'fontsize':50})
    ax.set_xlabel('Page Views', fontdict = {'fontsize':50})
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig





def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    df_bar['mes'] =df.index.strftime("%B")
    df_bar['anno']= df.index.strftime("%Y")

    # Draw bar plot

    #dir(df.index)
    fig, ax = plt.subplots(figsize= (20,20))

    df.plot(ax = ax, )

    sns.barplot(x = 'anno', y ='value'  , data = df_bar, hue ='mes' , 
                palette = 'hls', 
                capsize = 0.05, 
                saturation = 8, 
                errcolor = 'gray', 
                errwidth = 2,
                ci = 'sd' )

    ax.set_title('Months', fontdict = {'fontsize':30})
    ax.set_ylabel('Average Page Views', fontdict = {'fontsize':30})
    ax.set_xlabel('Years', fontdict = {'fontsize':30})


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
    
    # Dividimos el gráfico en dos
    fig, axes = plt.subplots(1, 2,figsize= (30,10))

    # Fijamos los titulos
    axes[0].set_title("Year-wise Box Plot (Trend)", fontdict = {'fontsize':40})
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontdict = {'fontsize':40})

    # Graficamos a la izquierda
    sns.boxplot(x = 'year', y = 'value',data = df_box, ax = axes[0])
    sns.boxplot(x = 'month', y = 'value',data = df_box, ax = axes[1])

    # Titulamos los ejes
    axes[0].set_ylabel('Average Page Views', fontdict = {'fontsize':30})
    axes[0].set_xlabel('Year', fontdict = {'fontsize':30})

    axes[1].set_ylabel('Average Page Views', fontdict = {'fontsize':30})
    axes[1].set_xlabel('Month', fontdict = {'fontsize':30})



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
