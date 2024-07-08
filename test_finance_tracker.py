import unittest
import pandas as pd
from main import add_income, add_expense, save_data, load_data, show_summary

class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(columns=['Amount', 'Source/Category', 'Type', 'Date'])

    def test_add_income(self):
        df = add_income(self.df, 1000, 'Salary', '2023-07-01')
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Amount'], 1000)
        self.assertEqual(df.iloc[0]['Source/Category'], 'Salary')
        self.assertEqual(df.iloc[0]['Type'], 'Income')
        self.assertEqual(df.iloc[0]['Date'], '2023-07-01')

    def test_add_expense(self):
        df = add_expense(self.df, 500, 'Groceries', '2023-07-02')
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Amount'], 500)
        self.assertEqual(df.iloc[0]['Source/Category'], 'Groceries')
        self.assertEqual(df.iloc[0]['Type'], 'Expense')
        self.assertEqual(df.iloc[0]['Date'], '2023-07-02')

    def test_save_and_load_data(self):
        df = add_income(self.df, 1000, 'Salary', '2023-07-01')
        df = add_expense(df, 500, 'Groceries', '2023-07-02')
        save_data(df, 'test_data.csv')
        loaded_df = load_data('test_data.csv')
        pd.testing.assert_frame_equal(df, loaded_df)

    def test_show_summary(self):
        df = add_income(self.df, 1000, 'Salary', '2023-07-01')
        df = add_expense(df, 500, 'Groceries', '2023-07-02')
        show_summary(df)
        total_income = df[df['Type'] == 'Income']['Amount'].sum()
        total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
        net_savings = total_income - total_expense
        self.assertEqual(total_income, 1000)
        self.assertEqual(total_expense, 500)
        self.assertEqual(net_savings, 500)

if __name__ == '__main__':
    unittest.main()