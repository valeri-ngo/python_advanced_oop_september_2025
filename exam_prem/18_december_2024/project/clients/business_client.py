from project.clients.base_client import BaseClient


class BusinessClient(BaseClient):
    MIN_ORDERS_CNT = 2
    MAX_DISCOUNT = 10.0
    MIN_DISCOUNT = 0.0

    def update_discount(self):
        self.discount = self.MAX_DISCOUNT if self.total_orders >= self.MIN_ORDERS_CNT else self.MIN_DISCOUNT