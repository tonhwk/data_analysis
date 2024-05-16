import pandas as pd
import plotly.graph_objects as go

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('cereal.csv')

# Display the first few rows of the DataFrame
print(df.head(1))

# Create a table figure with the first few rows of the DataFrame
fig = go.Figure(data=[go.Table(header=dict(values=df.columns),
                               cells=dict(values=df.head().values.T))])

# Show the table
fig.show()


