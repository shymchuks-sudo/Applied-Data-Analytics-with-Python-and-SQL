import pandas as pd
import plotly.express as px

data = {
    'Model': ['Model A', 'Model B', 'Model C', 'Model D'],
    'Accuracy': [0.85, 0.90, 0.75, 0.95],
    'F1 Score': [0.83, 0.88, 0.70, 0.92],
    'Training Time (s)': [120, 150, 90, 200]
}

df = pd.DataFrame(data)

# fig = px.bar(df,
#              x='Model',
#              y='Accuracy',
#              title='Model Accuracy Comparison',
#              color='Model',
#              text='Accuracy')

# fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

# fig = px.pie(df,
#              values='Training Time (s)',
#              names='Model',
#              title='Training Time Distribution by Model',
#              hover_data=['Accuracy', 'F1 Score'])

time_data = {
    'epoch': [1,2,3,4,5],
    'model a': [0.8, 0.85, 0.86, 0.78, 0.89],
    'model b': [0.79, 0.82, 0.85, 0.87, 0.9]
}
time_data = pd.DataFrame(time_data)
time_df_melted = time_data.melt(id_vars='epoch', var_name='model', value_name='Accuracy')
fig = px.line(time_df_melted,
              x='epoch',
              y='Accuracy',
              color='model',
              title='Model Accuracy Over Epochs')

fig.show()
