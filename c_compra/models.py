from typing import Optional
from sqlmodel import Field, SQLModel,Relationship


class Product(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    name: str
    price: float
    amount: int

class Cart(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    sale_cart_id: Optional[int] = Field(default=None, foreign_key="salecart.id", nullable=True)
    sale_cart: Optional["SaleCart"] = Relationship()
    # Adicione o sa_relationship_kwargs com o cascade aqui:
    itens: list["ItemCart"] = Relationship(
        back_populates="cart", sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

class ItemCart(SQLModel, table=True):
    cart_id: Optional[int] = Field(default=None, foreign_key="cart.id", primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
    amount: int = Field(default=1)
    
    cart: "Cart" = Relationship(back_populates="itens")
    product: "Product" = Relationship()

class SaleCart(SQLModel, table=True):
   id: Optional[int] | None = Field(default=None, primary_key=True)
   code: str
   discount: float #0.05 == 5%
