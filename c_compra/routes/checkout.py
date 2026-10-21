from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from schema import StandardResponse
from models import Cart, SaleCart
from engine import engine
'''
class PaymentMethod(StrEnum):
    PIX = "pix"
    CREDIT_CARD = "credit_card"

PAYMENT_DISCOUNT = {
    PaymentMethod.PIX: Decimal("0.05"),
    PaymentMethod.CREDIT_CARD: Decimal("0"),
}

def calculate_total(subtotal: Decimal, coupon_rate: Decimal, method: PaymentMethod) -> Decimal:
    total = subtotal * (1 - coupon_rate) * (1 - PAYMENT_DISCOUNT[method])
    return total.quantize(Decimal("0.01"))
'''
router_checkout = APIRouter(prefix="/checkout", tags=["Checkout"])

@router_checkout.post("/{cart_id}")
async def finalize_checkout(cart_id: int, payment_method: str):
    with Session(engine) as session:
        cart = session.get(Cart, cart_id)
        if not cart:
            raise HTTPException(status_code=404, detail="Cart not found")
        
        if not cart.itens:
            raise HTTPException(status_code=400, detail="Cart is empty")

        subtotal = sum(item.product.price * item.amount for item in cart.itens)
        
        coupon_code_applied = None
        discount_coupon_value = 0.0
        
        if cart.sale_cart_id:
            coupon = session.get(SaleCart, cart.sale_cart_id)
            if coupon:
                coupon_code_applied = coupon.code
                discount_coupon_value = subtotal * coupon.discount

        total_after_coupon = max(0.0, subtotal - discount_coupon_value)

        payment_discount_value = 0.0
        normalized_payment = payment_method.lower().strip()
        
        if normalized_payment == "pix":
            payment_discount_value = total_after_coupon * 0.05
        elif normalized_payment != "credit_card" and normalized_payment != "cartao":
            raise HTTPException(status_code=400, detail="Método de pagamento inválido. Escolha 'pix' ou 'credit_card'.")

        final_total = max(0.0, total_after_coupon - payment_discount_value)

        items_summary = [
            {
                "name": item.product.name if hasattr(item, "product") else f"Item {item.id}",
                "price": item.product.price,
                "amount": item.amount,
                "total": item.product.price * item.amount
            }
            for item in cart.itens
        ]

        checkout_data = {
            "cart_id": cart.id,
            "itens": items_summary,
            "subtotal": round(subtotal, 2),
            "coupon_applied": coupon_code_applied,
            "discount": round(discount_coupon_value, 2),
            "payment_method": normalized_payment,
            "payment_discount": round(payment_discount_value, 2),
            "final_amount": round(final_total, 2)
        }

        return StandardResponse(
            success=True,
            message="Checkout completed successfully!",
            data=checkout_data
        )