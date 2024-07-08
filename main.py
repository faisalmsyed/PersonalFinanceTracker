import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Welcome to the Personal Finance Tracker")

if __name__ == "__main__":
    main()

def add_income(df, amount, source):
    df = df.append({'Amount': amount, 'Source': source, 'Type':'Income'}, ignore_index=True)
    return df

def add_expense(df,amount, category):
    df = df.append({'Amount': amount, 'Category': category, 'Type': 'Expense'}, ignore_index=True)
    return df

def save_data(df, filename):
    df.to_csv(filename, index=False)

def load_data(filename):
    return pd.read_csv(filename)

def plot_data(df):
    income = df[df['Type'] == 'Income']
    expenses = df[df['Type'] == 'Expense']

    plt.figure(figsize=(10,5))
    plt.bar(income['Source'], income['Amount'], label='Income')
    plt.bar(expenses['Category'], expenses['Amount'], label='Expenses', alpha=0.7)
    plt.xlabel('Source/Category')
    plt.ylabel('Amount')
    plt.legend()
    plt.show()
