from exceptions.customer_not_found import CustomerNotFoundException
from models.customer import Customer
from stores.customer_store import CustomerStore


class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customers: dict[int, Customer] = {}

    def add_customer(self, customer: Customer):
        self.customers[customer.customer_id] = customer

    def get_all_customers(self):
        return list(self.customers.values())

    def get_customer(self, customer_id: int):
        if customer_id in self.customers:
            return self.customers[customer_id]
        raise CustomerNotFoundException(customer_id)

    def update_customer(self, customer_id: int, customer: Customer):
        if customer_id not in self.customers:
            raise CustomerNotFoundException(customer_id)
        self.customers[customer_id] = customer
        return customer

    def delete_customer(self, customer_id: int):
        if customer_id not in self.customers:
            raise CustomerNotFoundException(customer_id)
        del self.customers[customer_id]