import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

corr_data = pd.DataFrame({
    'Feature1': [1.3, 0.8, 0.6],
    'Feature2': [0.8, 1, 0.2],
    'Feature3': [0.6, 0.3, 1]
})

sns.heatmap(corr_data, annot=True, cmap='rocket')
plt.title("Custom Correlation Heatmap")
plt.show()
