from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    """Represents a physical address with street, city, state, and zip code"""
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    """Represents a person with a name and address"""
    id : int
    name : str
    email : str
    is_active : bool = True
    created_at : datetime
    address : Address
    tags : List[str] = []

