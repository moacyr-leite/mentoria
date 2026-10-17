from fastapi import FastAPI, HTTPException
from sqlmodel import (
    Field, select, SQLModel, Session, create_engine,
    Relationship
)
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: int
    amount: int

class Cart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    products: list["Product"] = Relationship()

#p_1 = Product(name="Mouse sem fio", price=7990, amount=5)
#p_2 = Product(name="Teclado mecânico", price=24990, amount=2)
#p_3 = Product(name="Fone de ouvido bluetooth", price=15990, amount=3)
#p_4 = Product(name="Webcam Full HD", price=19990, amount=1)
#p_5 = Product(name="Carregador USB-C", price=11990, amount=5)

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

'''
with Session(engine) as session:
    session.add(p_1)
    session.add(p_2)
    session.add(p_3)
    session.add(p_4)
    session.add(p_5)
    session.commit()

with Session(engine) as session:
    statement = select(Product).where(Product.name == "Mouse sem fio")
    product = session.exec(statement).first()
    print(product)
'''

app = FastAPI()

#CRUD PRODUCT

##CREATE
@app.post("/products")
async def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
##READ
@app.get("/products")
def read_products():
    with Session(engine) as session:
        query = select(Product)
        products = session.exec(query).all()
        return products
##UPDATE
@app.put("/products/{product_id}")
def update_product(product_id:int, product:Product):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404)
        db_product.name = product.name
        db_product.price = product.price
        db_product.amount = product.amount
        session.commit()
        return db_product
##DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404)
        session.delete(db_product)
        session.commit()
        return {"ok": True}

#CART
