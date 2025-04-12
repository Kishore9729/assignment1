from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_expenses(n):
    expenses = []
    for _ in range(n):
        expense = {
            'date': fake.date_this_month(),
            'amount': round(random.uniform(5.0, 500.0), 2),
            'category': random.choice(['Food', 'Entertainment', 'Utilities', 'Transport', 'Shopping', 'Health', 'Other']),
            'description': fake.text(max_nb_chars=20)
        }
        expenses.append(expense)
    return expenses

monthly_expenses = {f"month_{i+1}": pd.DataFrame(generate_expenses(100)) for i in range(12)}

# Save each month's expenses as a CSV for easy loading into a database
for month, df in monthly_expenses.items():
    df.to_csv(f"{month}_expenses.csv", index=False)
