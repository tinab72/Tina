# This is the file related to Hands On Lab TDD-BDD From TB
# 1.	Task 1: GitHub URL of the tests/factories.py showing the updated code for fake products (1 pt)

import factory
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
from models.product import product
import qrcode

    class ProductFactory(factory.Factory):
        """ Creates fake products """

        class Meta:
            model = Product

        id = factory.Sequence(lambda n: n)
        name = factory.Faker("name")
        price = factory.Faker("price")
        disabled = FuzzyChoice(choices=[True, False])
        date_purchase = FuzzyDate(date(2020, 1, 1))
        description = factory.Faker('Made in Italy')
        stock_quantity = factory.Faker('random_int', min=0, max=1500)

        @staticmethod
        def generate_qr_code(product_info):
        qr = qrcode.make(product_info)
        qr.save(f"product_{product_info['id']}_qr_code.png")
