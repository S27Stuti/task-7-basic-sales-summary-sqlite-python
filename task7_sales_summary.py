
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table and insert sample data
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
sample_data = [
    ('Laptop', 5, 700.0),
    ('Tablet', 10, 300.0),
    ('Smartphone', 8, 500.0),
    ('Monitor', 6, 200.0),
    ('Keyboard', 15, 50.0)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Query for sales summary
query = """
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Print and plot results
print(df)

# Plot bar chart
plt.figure(figsize=(10, 6))
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title('Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig("sales_chart.png")
