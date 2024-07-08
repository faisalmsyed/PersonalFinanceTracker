# Personal Finance Tracker

Welcome to the Personal Finance Tracker project! This tool helps you track your income and expenses, visualize your financial data, and provide summaries to better understand your financial health.

## Features

- **User Authentication:** Simple username and password protection.
- **Add Income and Expenses:** Interactively add your income sources and expense categories.
- **Data Validation:** Ensures valid inputs for amount and date.
- **Data Analysis:** Calculate total income, total expenses, and net savings.
- **Advanced Visualizations:** Plot monthly income and expenses, categorize expenses.
- **Data Export:** Save and load data to/from CSV files.
- **Summarized Reports:** View financial summaries and visualizations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/PersonalFinanceTracker.git
   cd PersonalFinanceTracker


2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install required libraries:**
   ```bash
   pip install pandas matplotlib
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

1. **Run the application and log in with the credentials:**
   - Username: `user`
   - Password: `pass`

2. **Options available:**
   - `1. Add Income` - Add an income entry.
   - `2. Add Expense` - Add an expense entry.
   - `3. Save` - Save the current data to a CSV file.
   - `4. Load` - Load data from a CSV file.
   - `5. Plot` - Visualize income and expense data.
   - `6. Summary` - View a summary of your financial data.
   - `7. Exit` - Exit the application.

3. **Adding Entries:**
   - Follow the prompts to enter amounts, sources/categories, and dates for income and expense entries.

4. **Saving and Loading Data:**
   - Use the `Save` option to save your data to a CSV file.
   - Use the `Load` option to load previously saved data.

5. **Viewing Summaries and Visualizations:**
   - Use the `Plot` option to visualize your data.
   - Use the `Summary` option to see a financial summary and monthly trends.

## Automated Testing
To run automated tests, execute the following command:
```bash
   python -m unittest test_finance_tracker.py
   ```


## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Please ensure any changes are well-documented.