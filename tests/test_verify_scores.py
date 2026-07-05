from database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT
    product_name,
    family,
    top_selling_score
FROM products
LIMIT 10
""")

rows = cursor.fetchall()

conn.close()

for row in rows:
    print(row)