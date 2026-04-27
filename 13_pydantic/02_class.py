from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True


product_one = Product(id=1, name='mobile', price=10000.0, in_stock = True)
product_two = Product(id=2, name='mouse', price=100.0, in_stock=False)

print(product_one)
print(product_two)