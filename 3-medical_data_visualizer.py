import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv',sep=',')

# 2
df['overweight'] = df['weight'] / (df['height']/100) **2
df.loc[df['overweight'] < 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1

# 3 
df.loc[(df['cholesterol'] == 1) | (df['gluc'] == 1),['cholesterol','gluc']] = 0
df.loc[(df['cholesterol'] > 1) | (df['gluc'] > 1),['cholesterol','gluc']] = 1


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars='cardio',var_name='variable',
    value_vars=['cholesterol','gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = pd.melt(df,var_name='variable',
    value_vars=['alco', 'active','cholesterol','gluc','overweight','smoke'],id_vars='cardio')
    
    # 7
    fig1 = sns.catplot(data=df_cat,kind='count',x='variable',hue='value',col='cardio').set_axis_labels('variable','total')
    
    # 8
    fig = fig1
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo']<=df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025))&
    (df['height'] <= df['height'].quantile(0.975))&
    (df['weight'] >= df['weight'].quantile(0.025))&
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(7,5))

    # 15
    sns.heatmap(corr,mask=mask,fmt='.1f',vmax=.3,linewidths=.5,square=True,cbar_kws = {'shrink':0.5},annot=True, center=0)


    # 16
    fig.savefig('heatmap.png')
    return fig
