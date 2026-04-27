from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    emp_id : int
    name : str = Field(
        ...,   
        min_length = 2,
        max_length = 50,
        description = 'Employee name',
        examples = 'Aakash'
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        ge = 10000,
        description = 'Employee salary',
        examples = 100000.0
    )

emp_data = {
    'emp_id' : 123,
    'name' : 'Aakash',
    'department' : 'IT',
    'salary' : 100000.0
}

emp = Employee(**emp_data)
print(emp)