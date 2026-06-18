
import pandas as pd
import random
from datetime import datetime, timedelta

categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Bills"
]

payment_modes = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card"
]

descriptions = [
    "Daily Expense",
    "Monthly Payment",
    "Purchase",
    "Utility Bill",
    "Travel Expense"
]

data = []

start_date = datetime(2025, 1, 1)

for i in range(1500):

    date = start_date + timedelta(days=random.randint(0, 180))

    category = random.choice(categories)

    if category == "Food":
        amount = random.randint(100, 800)

    elif category == "Travel":
        amount = random.randint(500, 3000)

    elif category == "Rent":
        amount = random.randint(8000, 20000)

    elif category == "Shopping":
        amount = random.randint(500, 5000)

    else:  # Bills
        amount = random.randint(300, 4000)

    payment_mode = random.choice(payment_modes)

    description = random.choice(descriptions)

    data.append([
        date.strftime("%Y-%m-%d"),
        category,
        amount,
        payment_mode,
        description
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Category",
        "Amount",
        "Payment Mode",
        "Description"
    ]
)

df.to_csv(
    "data/expenses.csv",
    index=False
)

print("Expense dataset created successfully!")


