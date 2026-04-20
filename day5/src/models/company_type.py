#create compamy typr enum
from enum import Enum


class CompanyType(str, Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    GOVERNMENT = "Government"