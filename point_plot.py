import seaborn as sns 
import matplotlib.pyplot as plt 
from numpy import median 


tips = sns.load_dataset('tips')

sns.catplot(x= 'day', y = 'tip', data = tips, kind = 'point', capsize = 0.2, join = False, ci = None)
sns.catplot(x= 'day', y = 'tip', data = tips, kind = 'point', capsize = 0.2, estimator= median, errorbar = None, linestyle = 'none')

#join = Fasle replaced by linestyle = 'none'
#ci = None replaced by errorbar = None
plt.show()