#design data validation for full name
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., pattern=r'^[A-Za-z]+$', min_length=1, max_length=50, description="First name of the customer")
    last_name: str = Field(..., pattern=r'^[A-Za-z]+$', min_length=1, max_length=50, description="Last name of the customer")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
