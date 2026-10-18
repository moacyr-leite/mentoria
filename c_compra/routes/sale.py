from engine import engine
from fastapi import APIRouter, HTTPException
from sqlmodel import (Session, select)
from models import Cart, SaleCart
from schema import StandardResponse

router_sale_cart = APIRouter(prefix="/salecart", tags=["SaleCart"])

#CRUD SaleCart

##CREATE
@router_sale_cart.post("/", response_model=StandardResponse[SaleCart])
async def create_sale_cart(sale_cart: SaleCart):
    with Session(engine) as session:
        session.add(sale_cart)
        session.commit()
        session.refresh(sale_cart)
        return StandardResponse(
            success=True,
            message="Success create SaleCart",
            data=sale_cart
        )
##READ
@router_sale_cart.get("/", response_model=StandardResponse[list[SaleCart]])
async def read_sale_carts():
    with Session(engine) as session:
        query = select(SaleCart)
        SaleCarts = session.exec(query).all()
        return StandardResponse(
                    success=True,
                    message="List SaleCart",
                    data=SaleCarts
                )
##UPDATE
@router_sale_cart.put("/{sale_cart_id}", response_model=StandardResponse[SaleCart])
async def update_sale_cart(sale_cart_id:int, sale_cart:SaleCart):
    with Session(engine) as session:
        db_sale_cart = session.get(SaleCart, sale_cart_id)
        if not db_sale_cart:
            raise HTTPException(status_code=404)
        db_sale_cart.code = sale_cart.code
        db_sale_cart.discount = sale_cart.discount
        session.commit()
        return StandardResponse(
                    success=True,
                    message="Success Update",
                    data=db_sale_cart
                )
##DELETE
@router_sale_cart.delete("/{sale_cart_id}", response_model=StandardResponse[None])
async def delete_sale_cart(SaleCart_id:int):
    with Session(engine) as session:
        db_sale_cart = session.get(SaleCart, SaleCart_id)
        if not db_sale_cart:
            raise HTTPException(status_code=404)
        session.delete(db_sale_cart)
        session.commit()
        return StandardResponse(
                    success=True,
                    message="Success delete",
                    data= None
                )

## FINISH
@router_sale_cart.post("/{cart_id}/apply-coupon")
async def apply_coupon(cart_id: int, coupon_code: str):
  with Session(engine) as session:
    cart = session.get(Cart, cart_id)
    if not cart:
      raise HTTPException(status_code=404, detail="Cart not found")
    query = select(SaleCart).where(SaleCart.code == coupon_code)
    coupon = session.exec(query).first()

    if not coupon:
      raise HTTPException(
          status_code=404, detail="Coupon invalid or not found"
      )

    # Associa o cupom ao carrinho
    cart.sale_cart_id = coupon.id
    #session.add(cart)
    session.commit()
    session.refresh(cart)

    return StandardResponse(
        success=True, 
        message="Coupon applied successfully!", 
        data=cart
    )