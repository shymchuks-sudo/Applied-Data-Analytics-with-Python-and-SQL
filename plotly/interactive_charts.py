import pandas as pd
import plotly.express as px

data = {
    'Model': ['Model A', 'Model B', 'Model C', 'Model D'],
    'Accuracy': [0.85, 0.90, 0.75, 0.95],
    'F1 Score': [0.83, 0.88, 0.70, 0.92],
    'Training Time (s)': [120, 150, 90, 200]
}

df = pd.DataFrame(data)
print(df.head())
#      Model  Accuracy  F1 Score  Training Time (s)
# 0  Model A      0.85      0.83                120
# 1  Model B      0.90      0.88                150
# 2  Model C      0.75      0.70                 90
# 3  Model D      0.95      0.92                200

fig = px.scatter(df,
                 x='Accuracy',
                 y='F1 Score',
                 color='Model',
                 size='Training Time (s)',
                 hover_name='Model',
                 title='Accuracy vs F1 Score',
                 size_max=60)

fig.show()
