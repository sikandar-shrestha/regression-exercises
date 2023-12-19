#standard ds imports
import pandas as pd
import numpy as np

#viualization imports
import matplotlib.pyplot as plt
import seaborn as sns




def plot_variable_pairs(df):
    
    # reg = regression line (or best fitting line)
    sns.pairplot(df,
                 diag_kws={'color':'green'},
                 kind='reg',
                 plot_kws={'line_kws':{'color': 'red'}},
                 corner=True
                )
    
    plt.show()
    
    
    
    
    
def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    
    
    for i in categorical_var:
        
        for j in continuous_var:
        
            plt.figure(figsize=(15, 8))
            # Plotting boxplot
            plt.subplot(1, 4, 1)
            sns.boxplot(x=i, y=j, data=df)
            plt.title('Boxplot')

            # Plotting bar plot
            plt.subplot(1, 4, 2)
            sns.barplot(x=i, y=j, data=df)
            plt.title('bar Plot')

            # Plotting scatter plot (for smaller datasets)
            plt.subplot(1, 4, 3)
            sns.scatterplot(x=i, y=j, data=df)
            plt.title('scatter Plot')
            
            # Plotting swarm plot (for smaller datasets)
            plt.subplot(1, 4, 4)
            sns.swarmplot(x=i, y=j, data=df)
            plt.title('swarm Plot')
            
            # Plotting strip plot (for smaller datasets)
            # plt.subplot(2, 2, 5)
            # sns.stripplot(x=i, y=j, data=df)
            # plt.title('strip Plot')
            

            plt.tight_layout()
            plt.show()