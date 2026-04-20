#create corporate class inheriting from customer with pydantic validation
from pydantic import Field
from models.customer import Customer
from models.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType
    registration_no: str = Field(..., description="Company registration number")