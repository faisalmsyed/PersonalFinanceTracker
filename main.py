import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Welcome to the Personal Finance Tracker")
    if not authenticate_user():
        print("Authentication failed. Exiting.")
        return

df = pd.DataFrame(columns = ['Amount', 'Source/Category', 'Type', 'Date'])

def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username == "user" and password == "pass"

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount. Please enter a positive number.")

def add_income(df, amount, source, date):
    df = df.append({'Amount': amount, 'Source/Category': source, 'Type': 'Income', 'Date': date}, ignore_index=True)
    return df

def add_expense(df, amount, category, date):
    df = df.append({'Amount': amount, 'Source/Category': category, 'Type': 'Expense', 'Date': date}, ignore_index=True)
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

def show_summary(df):
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    net_savings = total_income - total_expense

    print(f"\nSummary:\nTotal Income: ${total_income:.2f}\nTotal Expenses: ${total_expense:.2f}\nNet Savings: ${net_savings:.2f}")

    plot_monthly_summary(df)

def plot_monthly_summary(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    monthly_summary = df.resample('M').sum()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_summary.index, monthly_summary['Amount'], label='Total')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Monthly Financial Summary')
    plt.legend()
    plt.show()

while True:
    print("\nOptions: 1. Add Income  2. Add Expense  3. Save  4. Load  5. Plot  6. Summary  7. Exit")
    choice = input("Choose an option:")

    if choice == '1':
        amount = get_valid_amount()
        source = input("Enter source: ")
        date = input("Enter date (YYYY-MM-DD): ")
        df = add_income(df, amount, source, date)
    elif choice == '2':
        amount = get_valid_amount()
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        df = add_expense(df, amount, category, date)
    elif choice == '3':
        filename = input("Enter filename: ")
        save_data(df, filename)
    elif choice == '4':
        filename = input("Enter filename: ")
        df = load_data(filename)
    elif choice == '5':
        plot_data(df)
    elif choice == '6':
        show_summary(df)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()