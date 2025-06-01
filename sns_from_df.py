# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 


# tips =
# Create a DataFrame from csv file
# df = pd.read_csv(csv_filepath)
fig, axes = plt.subplots(2,2, figsize = (14,10))
#load seaborn inbuilt dataset 
df = sns.load_dataset("tips")
df.head()
# plt.figure()
hue_colors = {"Yes":'b', 'No': 'r'}
# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='sex', data = df
              ,ax = axes[0,0]
              , hue = 'smoker',
              palette = hue_colors #this line further divides the bars into two colors scatter plot ma chai no need as all data points are individual
              )

# Display the plot
# plt.show()

# plt.figure()

sns.scatterplot(x= 'total_bill', y= 'tip',
                data = df , hue = 'smoker', 
                hue_order = ['Yes','No'],
                palette = hue_colors,
                ax = axes[0,1]
                )

fig.suptitle('All required figures', fontsize = 10)
# `fig.tight_layout()` is a function in Matplotlib that automatically adjusts the subplot parameters
# to give specified padding between the subplots and around the figure. It helps to prevent
# overlapping of subplots or axis labels, making the plot more visually appealing and easier to read.
fig.tight_layout()     # minimizes the distance betweent the figure window border and the internal subplot borders
fig.subplots_adjust(hspace= 0.2)  #adjusts the horizontal space betwn two rows of the sub-plots



plt.show()
# """ """