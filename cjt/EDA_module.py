import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

class PropertyCheck:
    def __init__(self, df:pd.DataFrame, columns:list):
        self.df = df
        self.columns = columns

    
    def check_stats(self):
        # indicator_list의 기술통계량
        for col in self.columns: 
        
            print(f'{col}')
            print(self.df[col].describe())
            print()
            
    def check_boxplot(self):
        # indicator_list의 box plot
        fig, axs = plt.subplots(1, len(self.columns), figsize=(15,5))
        
        for i, col in enumerate(self.columns): 
            sns.boxplot(data=self.df, x=col, ax=axs[i])
        plt.show()