from pathlib import Path
import sqlite3
import pandas as pd

# Create a sqlite db
Path('my_data.db').touch()

# create sqlit connection
conn = sqlite3.connect('my_data.db')
c = conn.cursor()

# load data to db
categories = pd.read_csv('data/BigSupplyCo_Categories.csv')
categories.to_sql('categories', conn, index=False)

customers = pd.read_csv('data/BigSupplyCo_Customers.csv')
customers.to_sql('customers', conn, index=False)

departments = pd.read_csv('data/BigSupplyCo_Departments.csv')
departments.to_sql('departments', conn, index=False)

orders = pd.read_csv('data/BigSupplyCo_Orders.csv', encoding='latin-1')
orders.to_sql('orders', conn, index=False)

products = pd.read_csv('data/BigSupplyCo_Products.csv')
products.to_sql('products', conn, index=False)