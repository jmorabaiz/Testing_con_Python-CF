import unittest
from entities.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        # print('>>> El método setUp se ejecuta antes de cada una de las pruebas.')
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo sentimos el precio no es el mismo')

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name)  # Regex

    # python -m unittest entities.test.test_product.TestProduct.test_product_example -v
    # python -m unittest discover -v (Run all the test)
    def test_product_example(self):
        self.assertEqual(1, 1)


# if __name__ == '__main__':
#     unittest.main()

# coverage run -m unittest discover -v
# coverage report -m
# coverage html
