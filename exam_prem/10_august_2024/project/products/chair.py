from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL_TYPE = 'Wood'
    SUB_TYPE = 'Furniture'
    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL_TYPE, self.SUB_TYPE)

    def discount(self):
        self.price *= 0.9