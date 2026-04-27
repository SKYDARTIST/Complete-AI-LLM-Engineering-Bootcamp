from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool


input_data = {"id":1, "name":"John Doe", "is_active":True}

user_obj = User(**input_data)
# ** symbols used to unpack the dictionary values

print(user_obj)