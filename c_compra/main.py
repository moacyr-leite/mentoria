from fastapi import FastAPI
from sqlmodel import SQLModel
from routes.product import router_product
from routes.cart import router_cart
from routes.sale import router_sale_cart
from routes.checkout import router_checkout
from engine import engine


app = FastAPI()


app.include_router(router_product)
app.include_router(router_cart)
app.include_router(router_sale_cart)
app.include_router(router_checkout)

SQLModel.metadata.create_all(engine)