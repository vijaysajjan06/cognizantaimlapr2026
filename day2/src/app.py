# creating entry point for the application
from store.customerstore import CustomerStore
from view.customerview import CustomerView
"""
creating entry point for the application to display a random name.
"""


def check():
    """
    this function will display a random name using faker library.

    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()


if __name__ == "__main__":
    check()
