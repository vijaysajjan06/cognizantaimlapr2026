#create customer csv data loader class inheriting from customer data loader
import pandas as pd
from models.full_name import FullName
from models.customer import Customer
from stores import customer_store_impl
from dataloaders.customer_data_loader import CustomerDataLoader
class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: customer_store_impl):
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = int(row['phone_no'])
            full_name = FullName(first_name=first_name, last_name=last_name)
            customer = Customer(customer_id=customer_id, name=full_name, email=email, phone_no=phone_no)
            customer_store.add_customer(customer)
            