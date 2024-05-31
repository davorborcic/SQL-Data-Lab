from unittest import TestCase

from faker import Faker
import os
import logging as log
import faker_demo
import process_prod_codes_file


class Test(TestCase):
    def setUp(self):
        self.conn = faker_demo.create_connection()
        self.f = Faker()
        self.categories = process_prod_codes_file.process_google_prod_codes("data/taxonomy-with-ids.en-US.txt")

    def test_create_fake_customer(self):
        customer = (faker_demo.create_fake_customer(self.f))
        log.warning(customer)

    def test_create_fake_product(self):
        product = (faker_demo.create_fake_product(self.f))
        log.warning(product)

    def test_create_fake_transaction(self):
        transaction = (faker_demo.create_fake_transaction(self.f))
        log.warning(transaction)

    def test_create_fake_trans_detail(self):
        trans_detail = (faker_demo.create_fake_trans_detail(100, 1000, 200, 12000))
        log.warning(trans_detail)

    def test_create_connection(self):
        self.assertIsNotNone(self.conn)

    def test_close_connection(self):
        faker_demo.close_connection(self.conn)

    def test_process_google_prod_codes(self):
        prod_fields = process_prod_codes_file.process_google_prod_codes("data/taxonomy-with-ids.en-US.txt")
        print(prod_fields)
        self.fail()

    def test_generate_csv_list_of_prod_categories(self):
        filename = "prod_categories.csv"
        process_prod_codes_file.generate_csv_list_of_prod_categories(self.categories, filename)
        self.assertTrue(os.path.exists(f"data/{filename}"))


    def test_get_random_prod_cat(self):
        prod_cat = faker_demo.get_random_prod_cat(self.conn.cursor())
        log.warning(f"Product Category: {prod_cat}")
        self.assertIsNotNone(prod_cat)

