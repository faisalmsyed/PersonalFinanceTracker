import unittest
import pandas as pd
from main import add_income, add_expense

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

if __name__ == '__main__':
    unittest.main()
