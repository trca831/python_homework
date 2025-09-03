import sqlite3
import pandas as pd

### Task5

conn = sqlite3.connect(":memory:") 

# Create tables
conn.execute("CREATE TABLE products (product_id INTEGER PRIMARY KEY, product_name TEXT, price REAL)")
conn.execute("CREATE TABLE line_items (line_item_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER)")

# Insert sample data
conn.execute("INSERT INTO products VALUES (1, 'Widget', 10.0), (2, 'Gadget', 20.0)")
conn.execute("INSERT INTO line_items VALUES (1, 1, 2), (2, 2, 3), (3, 1, 1)")

# Read into DataFrame and continue logic
df = pd.read_sql_query("""
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    products.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
""", conn)

conn.close()

df['total'] = df['quantity'] * df['price']
summary_df = df.groupby('product_id').agg(
    line_item_count=('line_item_id', 'count'),
    total_sales=('total', 'sum'),
    product_name=('product_name', 'first')
).reset_index()
summary_df = summary_df.sort_values(by='product_name')
print(summary_df)