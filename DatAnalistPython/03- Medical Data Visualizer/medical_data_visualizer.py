import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column

# Tenemos el peso ya en kilos en la base de datos, pero la altura está en cm
IBM = df['weight']/((df['height']*0.01)**2)
# Lo clasificacmos en gente con y sin sobrepeso
Sobrepeso = IBM>25
# Lo pasamos a una notacion de 0 y 1
Sobrepeso= Sobrepeso.astype('int')

df['overweight'] = Sobrepeso

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']= np.where(df['cholesterol']>1, 1, 0)
df['gluc']= np.where(df['gluc']>1, 1, 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    vindependientes = ['cholesterol', 'gluc', 'smoke', 'alco','active', 'overweight']
    df_cat = pd.melt(df, id_vars='cardio'],value_vars=vindependientes, var_name='Variable', value_name='Valor')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['Variable', 'Valor', 'cardio'])['Valor'].count()).rename(columns={'Valor': 'Total'}).reset_index()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x="Variable",col="cardio", y="Total", kind="bar", hue="Valor" )


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi'])
            &(df['height']>=df['height'].quantile(0.025))
            &(df['height']<=df['height'].quantile(0.975))
            &(df['weight']>=df['weight'].quantile(0.025))
            &(df['weight']>=df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    # mask = np.triu(corr)

    # Set up the matplotlib figure
    # Draw the heatmap with 'sns.heatmap()  
  
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(7, 5))
        ax  = sns.heatmap(corr, mask=mask, vmax=.3, square=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
