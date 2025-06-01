import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

tips = sns.load_dataset("tips")
tips.head()
tips.value_counts('day')
sns.relplot(x = 'total_bill',
            y = 'tip',
            data = tips,
            kind = 'scatter',
            col = 'day',
            # col_wrap = 4,  # per row i.e 4 ta column aauxa
            row = 'smoker',
            col_order = ['Sat','Sun','Thur','Fri'],
            row_order= ['No','Yes'] 
            # hue = 'smoker'
            
            )

plt.tight_layout()
plt.show()

