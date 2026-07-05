TABLES = [

"""
CREATE TABLE IF NOT EXISTS products (

id INTEGER PRIMARY KEY AUTOINCREMENT,

product_name TEXT,

price REAL,

sold_count INTEGER DEFAULT 0,

category TEXT,

image TEXT,

family TEXT,

top_selling_score REAL DEFAULT 0,

evergreen_score REAL DEFAULT 0,

seasonal_score REAL DEFAULT 0,

opportunity_score REAL DEFAULT 0,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

""",

"""
CREATE TABLE IF NOT EXISTS settings (

id INTEGER PRIMARY KEY AUTOINCREMENT,

setting_name TEXT,

setting_value TEXT

);

"""

]