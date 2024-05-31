import pandas as pd

import random
from datetime import date

from dotenv import load_dotenv
from faker import Faker
import os
import mysql.connector
from mysql.connector import Error
import logging as log
import csv


load_dotenv()
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')


QUERY_PRODCAT = """
SELECT category_name 
FROM ProductCategories
ORDER BY 1
"""

if __name__ == '__main__':
    import faker_demo as ft
    QUERY_PRODCAT = """
    SELECT category_name 
    FROM ProductCategories
    ORDER BY 1
    """

    connection = ft.create_connection()

    print("Example of using Pandas for data retrieval")
    test_frame = pd.read_sql(QUERY_PRODCAT, connection)

    print(test_frame)

    cursor = connection.cursor()
    cursor.execute(QUERY_PRODCAT)
    records = cursor.fetchall()

    print("\nExample of using direct SQL statement for data retrieval")
    print(f"Printing first 10 retrieved records out of {len(records)}\n")
    for i in (range(10)):
        print(records[i][0])


    ft.close_connection(connection)