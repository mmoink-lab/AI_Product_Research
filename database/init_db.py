from database.db import get_connection
from database.models import TABLES


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    for table in TABLES:

        cursor.execute(table)

    conn.commit()

    conn.close()