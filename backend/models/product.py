from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    category: str
    stock: int
    description: str
    tags: list[str]