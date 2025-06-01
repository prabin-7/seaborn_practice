import seaborn as sns 
import matplotlib.pyplot as plt

height = [62, 64, 66, 75, 66,68, 65, 71, 76,71]

weight =[120, 136, 148, 175, 137,165,154, 172, 200, 187]

sns.scatterplot(x= height, y= weight)
plt.show()

sns.countplot(y= height)
plt.show()