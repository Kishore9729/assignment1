import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSVs
monthly_dfs = [pd.read_csv(f"month_{i+1}_expenses.csv") for i in range(12)]
all_expenses = pd.concat(monthly_dfs)

# Basic EDA
print(all_expenses.describe())

# Total expenses per category
category_expenses = all_expenses.groupby('category')['amount'].sum().reset_index()

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='amount', data=category_expenses)
plt.title('Total Expenses by Category')
plt.xticks(rotation=45)
plt.show()
