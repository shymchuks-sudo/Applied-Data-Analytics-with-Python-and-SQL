import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61]
}
tips = pd.DataFrame(data)

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter Plot of Total Bill vs. Tip")
plt.show()
