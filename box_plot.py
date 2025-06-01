#by default whiskers extend to 1.5* the interquratile range
#iqr = 25th to 75th distribution of data
#whis = 2.0, whis = [5,95], whis = [0,100]


import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')

fig,ax = plt.subplots(1,2,figsize = (10,6))  #figsize controls the over all figure size in inches ?  ## need to pass  height=6, aspect=1.5 for .catplot

ax[1] = sns.boxplot(x= 'day', y= 'tip', data = tips, whis =2.0, ax = ax[1], showfliers = False, hue = 'sex')   #sym = '', doesnot work while ploting on axes (not this reason but sym has been depreciatied and need to use #showfliers =True/False)
# sns.catplot(x= 'day', y= 'tip', data = tips, kind = 'box',whis = [30,100], showfliers = False)
sns.catplot(x= 'day', y= 'tip', data = tips, kind = 'violin', inner = 'quart')  #inner = ['box', 'stick', None, 'point', 'quart'] yeti madhya huna paro
#also catplot and relplot return a FacetGrid and donot accept ax parameters
plt.show()