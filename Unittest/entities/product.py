class ProductDiscountError(Exception):
    pass


class Product:

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price

        if discount > price:
            raise ProductDiscountError('Lo sentimos en descuento no puede mayor al precio')
            # assert  tiene su equivalente
        self.discount = discount

    @property
    def code(self):
        return f'code-{self.name}'
