import unittest
from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


def is_available_to_skip():
    return True


def is_connected():
    return False


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # print('>>> El método setUpClass se ejecuta antes de todas las pruebas.')
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # print('>>> El método setUpClass se ejecuta después de todas las pruebas.')
        pass

    def setUp(self) -> None:
        # print('>>> El método setUp se ejecuta antes de cada una de las pruebas.')
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self) -> None:
        # print('>>> El método tearDown se ejecuta después de cada una de las pruebas.')
        pass

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no está vacío.')

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse((self.shopping_cart_2.empty()))

    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price=700.0, discount=70.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price=1000.0, discount=0.0))

        self.assertGreater(self.shopping_cart_1.total, 0)  # >
        self.assertLess(self.shopping_cart_1.total, 2000)  # <
        self.assertEqual(self.shopping_cart_1.total, 1645.00)

    def test_total_empty_shopping_cart(self):
        # Se inicializa sin productos
        self.assertEqual(self.shopping_cart_1.total, 0.00)

    @unittest.skip('La prueba con cumple con los requerimientos necesarios')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # skipIf -> Evalúa sobre Verdadero
    # skipUnless -> Evalúa sobre Falso
    @unittest.skipIf(is_available_to_skip(), 'No se cuenta con todos los requerimientos')
    def test_skip_example_2(self):
        pass

    @unittest.skipUnless(is_connected(), 'No se cuenta con todos los requerimientos')
    def test_skip_example_3(self):
        pass


if __name__ == '__main__':
    unittest.main()
