import random

from faker import Faker


class MockData(Faker):
    categories = ['Food', 'Electronics', 'Cosmetics', 'Automotive', 'Furniture']


    @staticmethod
    def product_category():
        return random.choice(MockData.categories)

    def __init__(self, **config):
        super().__init__(**config)


if __name__ == '__main__':
    data = MockData()

    print(f"Example of product '{data.catch_phrase()}' in product category '{data.product_category()}'")