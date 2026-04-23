import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

data = StringIO("""
OrderID,Date,Product,Category,Sales,Quantity,City,Payment_Mode
1,2023-01-05,Laptop,Electronics,50000,1,Mumbai,UPI
2,2023-01-10,Phone,Electronics,20000,2,Delhi,Credit Card
3,2023-01-15,Tablet,Electronics,15000,1,Bangalore,Debit Card
4,2023-02-05,Table,Furniture,12000,1,Mumbai,Cash
5,2023-02-10,Chair,Furniture,4000,3,Delhi,UPI
6,2023-02-18,Sofa,Furniture,30000,1,Bangalore,Credit Card
7,2023-03-02,Headphones,Electronics,3000,2,Mumbai,UPI
8,2023-03-10,Keyboard,Electronics,2500,4,Delhi,Debit Card
9,2023-03-15,Mouse,Electronics,1500,5,Bangalore,Cash
10,2023-04-01,Monitor,Electronics,12000,2,Mumbai,UPI
11,2023-04-08,Bed,Furniture,35000,1,Delhi,Credit Card
12,2023-04-20,Wardrobe,Furniture,40000,1,Bangalore,Debit Card
13,2023-05-03,Laptop,Electronics,55000,1,Mumbai,UPI
14,2023-05-10,Phone,Electronics,22000,2,Delhi,Cash
15,2023-05-18,Chair,Furniture,5000,4,Bangalore,UPI
16,2023-06-01,Table,Furniture,15000,1,Mumbai,Credit Card
17,2023-06-10,Headphones,Electronics,3500,3,Delhi,Debit Card
18,2023-06-15,Sofa,Furniture,28000,1,Bangalore,Cash
19,2023-07-05,Monitor,Electronics,14000,2,Mumbai,UPI
20,2023-07-12,Keyboard,Electronics,3000,5,Delhi,Credit Card
""")

df = pd.read_csv(data)

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())

total_sales = df["Sales"].sum()
print(total_sales)

product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales.sort_values(ascending=False))

city_sales=df.groupby("City")["Sales"].sum()
print(city_sales.sort_values(ascending=False))

city_sales = df.groupby("City")["Sales"].sum()

city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

print(df[["Date","Month"]].head())

monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

monthly_sales.plot(kind="line",marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

payment_sales = df.groupby("Payment_Mode")["Sales"].sum()
print(payment_sales.sort_values(ascending=False))



























