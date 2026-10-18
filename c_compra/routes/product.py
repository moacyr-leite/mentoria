from engine import engine
from fastapi import APIRouter, HTTPException
from sqlmodel import (Session, select)
from models import Product
from schema import StandardResponse

router_product = APIRouter(prefix="/product", tags=["Product"])

#CRUD PRODUCT

##CREATE
@router_product.post("/", response_model=StandardResponse[Product])
async def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return StandardResponse(
            success=True,
            message="Success create product",
            data=product
        )
##READ
@router_product.get("/", response_model=StandardResponse[list[Product]])
async def read_products():
    with Session(engine) as session:
        query = select(Product)
        products = session.exec(query).all()
        return StandardResponse(
                    success=True,
                    message="List Product",
                    data=products
                )
##UPDATE
@router_product.put("/{product_id}", response_model=StandardResponse[Product])
async def update_product(product_id:int, product:Product):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404)
        db_product.name = product.name
        db_product.price = product.price
        db_product.amount = product.amount
        session.commit()
        return StandardResponse(
                    success=True,
                    message="Success Update",
                    data=db_product
                )
##DELETE
@router_product.delete("/{product_id}", response_model=StandardResponse[None])
async def delete_product(product_id:int):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404)
        session.delete(db_product)
        session.commit()
        return StandardResponse(
                    success=True,
                    message="Success delete",
                    data= None
                )

