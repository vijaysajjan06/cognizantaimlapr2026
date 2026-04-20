#display customers
import sys
import os
from faker import Faker

from configurations.configuration import Config
from dataloaders.customer_csv_dataloader import CustomerCSVDataLoader
from stores.customer_store_impl import CustomerStoreImpl

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

def display_customers(customer_store):
    config = Config()
    env = config.app_env
    if env == "Development":
        data_loader = CustomerCSVDataLoader()
        csv_path = os.path.join(project_root, "src", "resources", "customers.csv")
        data_loader.load_data(csv_path, customer_store)
        for customer in customer_store.get_all_customers():
            print(customer)
if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    display_customers(customer_store)
