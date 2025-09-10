import sqlite3

# Connect to the lesson database
conn = sqlite3.connect("../db/connect.db")  
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# Task 1
print("\nTask 1: Total price of first 5 orders")
task1_query = """
SELECT o.order_id,
       SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""
cursor.execute(task1_query)
for row in cursor.fetchall():
    print(row)  # (order_id, total_price)



# Task 2: 
print("\nTask 2: Average price of customer orders")
task2_query = """
SELECT c.name,
       AVG(sub.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b,
           SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS sub
ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
"""
cursor.execute(task2_query)
for row in cursor.fetchall():
    print(row)  



# Task 3
print("\nTask 3: Insert new order for Perez and Sons")

try:
    # Get customer_id
    cursor.execute("SELECT customer_id FROM customers WHERE name = 'Perez and Sons';")
    customer_id = cursor.fetchone()[0]

    # Get employee_id
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_id = cursor.fetchone()[0]

    # Get 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Begin transaction
    conn.execute("BEGIN;")

    # Insert into orders, return order_id
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert line_items (10 of each product)
    for pid in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, (order_id, pid, 10))

    # Commit transaction
    conn.commit()

    # Print the new line items
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.name
        FROM line_items AS li
        JOIN products AS p ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """, (order_id,))
    for row in cursor.fetchall():
        print(row)  # (line_item_id, quantity, product_name)

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)



# Task 4
print("\nTask 4: Employees with more than 5 orders")
task4_query = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""
cursor.execute(task4_query)
for row in cursor.fetchall():
    print(row)  # (employee_id, first_name, last_name, order_count)


# Close 
conn.close()