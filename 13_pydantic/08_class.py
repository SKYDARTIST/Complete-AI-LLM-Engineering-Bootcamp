from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street : str
    city : str
    state : str
    zipcode : str

class Person(BaseModel):
    id : int
    name : str
    age : int
    address : Address


address = Address(

    street = "123 Main St",
    city = "New York",
    state = "NY",
    zipcode = "12345"
)

user_one = Person(
    id = 1,
    name = "John Doe",
    age = 30,
    address = address
)

user = {
     "name" : "Jane Doe",
     "id" : 2,
    "age" : 25,
    "address" : {
        "street" : "456 Elm St",
        "city" : "Los Angeles",
        "state" : "CA",
        "zipcode" : "90001"
    }
}

user_obj = Person(**user)
print(user_obj)
