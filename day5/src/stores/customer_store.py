# customer store abstract class
from abc import ABC, abstractmethod
 
class CustomerStore(ABC):
    @abstractmethod
    def get_customer(self):
        pass
 
    @abstractmethod
    def get_all_customers(self):
        pass
 
    @abstractmethod
    def add_customer(self, customer: dict):
        pass
 
    @abstractmethod
    def update_customer(self, customer_id: int, customer: dict):
        pass
 
    @abstractmethod
    def delete_customer(self, customer_id: int):
        pass