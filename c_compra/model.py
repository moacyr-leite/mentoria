
from sqlmodel import Field, select, SQLModel, Session, create_engine

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: int
    amount: int

class Cart(SQLModel, table=True):
    products: list[Product] = []

p_1 = Product(name="Mouse sem fio", price=7990, amount=5)
p_2 = Product(name="Teclado mecânico", price=24990, amount=2)
p_3 = Product(name="Fone de ouvido bluetooth", price=15990, amount=3)
p_4 = Product(name="Webcam Full HD", price=19990, amount=1)
p_5 = Product(name="Carregador USB-C", price=11990, amount=5)

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

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

#CRUD PRODUCT

##CREATE
def create_product(name:str, price:int, amount:int):
    with Session(engine) as session:
        session.add(Product(
             name= name,
             price= price,
             amount= amount
        ))

##READ
def read_product(product_id):
    with Session(engine) as session:
            query = select(Product).where(Product.id == product_id)

            return session.exec(query).all()

##UPDATE
def update_product(product_id:int, name:str = None, price:int = None, amount:int = None):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        
        if name:
             product.name = name
        if price:
             product.price = price
        if amount:
             product.amount = amount


##DELETE
def delete_product(product_id:int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        
        session.delete(product)











