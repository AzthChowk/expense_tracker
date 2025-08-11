import pandas as pd
import plotly.express as px

# Load data from CSV
df = pd.read_csv('expenses_list.csv')  # Replace with your filename

# Ensure 'Amount' is numeric
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Group by 'Category' and sum 'Amount'
category_sums = df.groupby('Category')['Amount'].sum()
print(category_sums)

# # Plot using Plotly Express
# fig = px.bar(df, x='Category', y='Amount',
#              title='Total Amount Spent per Category',
#              labels={'Amount': 'Total Amount', 'Category': 'Expense Category'},
#              color='Category')

# fig.update_layout(xaxis_tickangle=-45)
# fig.show()
