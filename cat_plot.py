import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
tips.head()
sns.catplot(x= 'sex', y= 'tip', data =tips, errorbar ='ci', kind = 'bar' )
plt.show()