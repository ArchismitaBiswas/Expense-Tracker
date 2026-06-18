

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

df = pd.read_csv("data/expenses.csv")

print("\n===== EXPENSE TRACKER =====\n")

total_expense = df["Amount"].sum()

print("Total Expenses:", total_expense)

category_expense = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory Wise Expenses:\n")
print(category_expense)

highest_category = category_expense.idxmax()

print("\nHighest Spending Category:")
print(highest_category)

monthly_expense = (
    df.groupby(
        pd.to_datetime(df["Date"]).dt.month
    )["Amount"]
    .sum()
)

print("\nMonthly Expenses:\n")
print(monthly_expense)

with open("report/expense_report.txt", "w") as report:

    report.write("EXPENSE TRACKER REPORT\n")
    report.write("======================\n\n")

    report.write(f"Total Expenses: Rs. {total_expense}\n\n")

    report.write(f"Highest Spending Category: {highest_category}\n\n")

    report.write("CATEGORY-WISE EXPENSES\n\n")

    for category, amount in category_expense.items():
        report.write(f"{category}: Rs. {amount}\n")

    report.write("\nMONTHLY EXPENSES\n\n")

    for month, amount in monthly_expense.items():
        report.write(f"Month {month}: Rs. {amount}\n")

print("\nReport Generated Successfully!")


#Category Wise Expense Bar Chart
plt.figure(figsize=(8,5))

category_expense.plot(kind="bar")

plt.title("Category Wise Expenses")

plt.savefig(
    "charts/category_expenses.png"
)

plt.show()



#Payment Mode Distribution Pie Chart
plt.figure(figsize=(8,5))

df["Payment Mode"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Payment Mode Distribution")

plt.savefig(
    "charts/payment_mode_distribution.png"
)

plt.show()


#Monthly Expense Trend Line Chart
plt.figure(figsize=(8,5))

monthly_expense.plot(marker="o")

plt.title("Monthly Expense Trend")

plt.savefig(
    "charts/monthly_expense_trend.png"
)

plt.show()




