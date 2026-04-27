from pydantic import BaseModel
from typing import Optional,  List, Dict

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str, int]

class Blog(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None

cart_data = {
    'user_id' : 123,
    'items' : ['watch', 'charger', 'phone'],
    'quantities' : {'watch':1, 'charger':2, 'phone':1}
}


cart = Cart(**cart_data)
print(cart)

blog_data = {
    'title' : 'My first blog',
    'content' : 'This is the content of my first blog',
    'image_url' : 'https://example.com/image.jpg'
}

blog = Blog(**blog_data)
print(blog)

