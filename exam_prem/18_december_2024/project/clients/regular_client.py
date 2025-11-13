from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MIN_ORDERS_COUNT = 1
    MAX_DISCOUNT = 5.0
    MIN_DISCOUNT = 0.0

    def update_discount(self):
        self.discount = self.MAX_DISCOUNT if self.total_orders >= self.MIN_ORDERS_COUNT else self.MIN_DISCOUNT
