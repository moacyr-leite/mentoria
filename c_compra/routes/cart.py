from engine import engine
from fastapi import APIRouter, HTTPException
from sqlmodel import (Session, select)
from sqlalchemy.orm import selectinload
from models import Cart, ItemCart, Product, SaleCart
from schema import StandardResponse

router_cart = APIRouter(prefix="/cart", tags=["Cart"])

def change_product(cart_id, product_id, amount):
    statement = select(ItemCart).where(
            ItemCart.cart_id == cart_id,
            ItemCart.product_id == product_id
    )
    
    with Session(engine) as session:
        db_item_cart = session.exec(statement).first()
        
        if not db_item_cart:
            if amount <= 0:
                raise HTTPException(status_code=400)
            new_item_cart = ItemCart(
                cart_id=cart_id,
                product_id=product_id,
                amount=amount
            )
            product = session.get(Product, product_id)
            if product and product.amount - amount >= 0:
                product.amount -= amount
                session.add(new_item_cart)
                session.commit()
                return db_item_cart
            else:
                raise HTTPException(status_code=400)

        
        product = session.get(Product, product_id)
        if product and product.amount - amount >= 0:
            product.amount -= amount
            db_item_cart.amount += amount
            
        session.commit()
        return db_item_cart

#CRUD CART

##CREATE
@router_cart.post("/", response_model=StandardResponse[Cart])
async def create_cart(cart: Cart):
    with Session(engine) as session:
        if session.get(Cart, cart.id):
            raise HTTPException(status_code=400, detail="Existing cart!")
        session.add(cart)
        session.commit()
        session.refresh(cart)
        return StandardResponse(
            success=True,
            message="Sucess create cart",
            data=cart
        )

##READ
@router_cart.get("/", response_model=StandardResponse[list[Cart]])
async def read_carts():
    with Session(engine) as session:
        query = select(Cart)
        carts = session.exec(query).all()
        return StandardResponse(
            success=True,
            message="",
            data=carts
        )

@router_cart.get("/{cart_id}", response_model=StandardResponse[list[ItemCart]])
async def read_cart(cart_id):
    with Session(engine) as session:
        cart = session.get(Cart, cart_id).itens
        return StandardResponse(
            success=True,
            message="",
            data=cart
        )

"""##UPDATE #######################################
@router_cart.put("/")
async def update_cart(cart:Cart):
    with Session(engine) as session:
        db_cart = session.get(Cart, cart.id)
        if not db_cart:
            raise HTTPException(status_code=400)
        db_cart.itens = cart.itens
        session.commit()
"""

##DELETE
@router_cart.delete("/{cart_id}", response_model=StandardResponse[None])
async def delete_cart(cart_id: int):
  with Session(engine) as session:
    db_cart = session.get(Cart, cart_id)
    if not db_cart:
      raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    for i in db_cart.itens:
      db_product = session.get(Product, i.product_id)
      if db_product:
        db_product.amount += i.amount
        session.add(db_product)

    session.delete(db_cart)
    session.commit()

    return StandardResponse(
        success=True, 
        message="Delete cart success, estoque retornado", 
        data=None
    )

# ItemCart
@router_cart.post("/add", response_model=StandardResponse[ItemCart])
async def add_product(cart_id: int, product_id:int, amount: int = 1):
    change = change_product(cart_id, product_id, amount)
    if change:
        return StandardResponse(
            success=True,
            message="Product add to cart",
            data=change
        )
    else:
        return StandardResponse(
            success=False,
            message="DEDE",
            data=change
        )

@router_cart.post("/remove", response_model=StandardResponse[ItemCart|None])
async def remove_product(cart_id: int, product_id:int, amount: int = 1):
    change = change_product(cart_id, product_id, -amount)
    if change:
        return StandardResponse(
            success=True,
            message="Product remove to cart",
            data=change
        )
    else:
        return StandardResponse(
            success=False,
            message="DEDE",
            data=change
        )
