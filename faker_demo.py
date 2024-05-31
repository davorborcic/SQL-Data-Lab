import random
from datetime import date

from dotenv import load_dotenv
from faker import Faker
import os
import mysql.connector
from mysql.connector import Error
import logging as log

# a set of insert statements for loading main database tables

INS_CUSTOMER = """
INSERT INTO sqllab.Customers
(first_name, last_name, email, phone, address, city, state, zip_code)
values(%s, %s, %s, %s, %s, %s, %s, %s);
"""

INS_PRODUCT = """
INSERT INTO sqllab.Products
(product_name, description, price, stock, company, prod_category)
VALUES(%s, %s, %s, %s, %s, %s);
"""

INS_TRANS = """
INSERT INTO sqllab.Transactions
(customer_id, transaction_date, total_amount)
VALUES(%s, %s, %s);
"""

INS_TDETAILS = """
INSERT INTO sqllab.TransactionDetails
(transaction_id, product_id, quantity, price)
VALUES(%s, %s, %s, %s);
"""

LOV_PRODCAT = """
SELECT category_name 
FROM ProductCategories
ORDER BY RAND() 
LIMIT 1
"""

# load parameters (database credentials) from .env file and set global variables
load_dotenv()
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')


def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        if connection.is_connected():
            log.warning("Successfully connected to the database")
    except Error as e:
        log.error(f"Error: '{e}'")

    return connection


def close_connection(connection):
    """ Close the database connection """
    if connection.is_connected():
        connection.close()
        log.warning("The database connection is closed")


def create_fake_product(f: Faker, prod_cat):
    """
    Structure:
    product_id: Primary key
    product_name: Name of the product.
    description: Detailed description of the product.
    price: Price of the product.
    stock: Stock quantity (quantity on hand)
    company: Vendor / Manufacturer.
    """
    return (f.catch_phrase(), f.text(100), round(random.uniform(10, 2500), 2), random.randint(0, 400),
            f.company(), prod_cat)


def create_fake_customer(f: Faker):
    """
    Structure:
    customer_id: Primary key.
    first_name, last_name: Customer's first and last names.
    email: Customer's email address (unique).
    phone: Customer's phone number.
    address, city, state, zip_code: Customer's address details.
    """
    return f.first_name(), f.last_name(), f.email(), f.phone_number(), f.address(), f.city(), f.state(), f.zipcode()


def create_fake_transaction(f: Faker):
    """
    Structure:
    transaction_id: Primary key.
    customer_id: Foreign key referencing the Customers table.
    transaction_date: Timestamp of when the transaction took place.
    total_amount: Total amount of the transaction

    The generator assumes there are 500 customer and 500 product records
    A more sophisticated approach would be to count the records in the respective tables
    """
    return (random.randint(1, 500), f.date_between(date(2023, 1, 1),
                                                   date(2023, 12, 31)), round(random.uniform(1, 500), 2))


def create_fake_trans_detail(num_transaction: int, num_products: int, max_quantity: int, max_price: float) -> tuple:
    """
    Structure:
    transaction_detail_id: Primary key.
    transaction_id: Foreign key referencing the Transactions table.
    product_id: Foreign key referencing the Products table.
    quantity: Quantity of the product in the transaction.
    price: Price of the product at the time of the transaction.
    """
    return (random.randint(1, num_transaction), random.randint(1, num_products),
            round(random.uniform(1, max_quantity)), round(random.uniform(1, max_price), 2))


def get_random_prod_cat(cursor):
    cursor.execute(LOV_PRODCAT)  # pick randomly a product category
    prod_cat = cursor.fetchone()
    return prod_cat[0]


def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        log.warning(f"Connected to database: {cursor.fetchone()}")

        fake = Faker()

        #
        num_customer = 500
        num_product = 500
        num_transactions = 10000
        num_transaction_details = 20000
        max_quantity = 1000
        max_price = 1500

        log.warning(f'Loading table Customers')
        for _ in range(num_customer):
            cursor.execute(INS_CUSTOMER, (create_fake_customer(fake)))

        log.warning(f'Loading table Product')
        for _ in range(num_product):
            prod_cat = get_random_prod_cat(cursor)
            cursor.execute(INS_PRODUCT, (create_fake_product(fake, prod_cat)))

        log.warning(f'Loading table Transactions')
        for _ in range(num_transactions):
            cursor.execute(INS_TRANS, create_fake_transaction(fake))

        log.warning(f'Loading table Transaction Details')
        for _ in range(num_transaction_details):
            cursor.execute(INS_TDETAILS,
                           create_fake_trans_detail(num_transactions, num_product, max_quantity, max_price))
        # Close the connection
        connection.commit()
        close_connection(connection)


if __name__ == '__main__':
    main()
