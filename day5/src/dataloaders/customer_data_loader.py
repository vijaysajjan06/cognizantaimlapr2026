#create customer data loader absract class
from abc import ABC, abstractmethod

from stores import customer_store_impl
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path, customer_store: customer_store_impl):
        pass
