from pprint import pprint

import requests

URL = "http://127.0.0.1:8000"

def exibir_estoque():
    response = requests.get(f"{URL}/product/").json()
    pprint(response)

if __name__ == "__main__":
    # Exibir Estoque
    exibir_estoque()
    
    cart_id = 2
    # Criar carrinho
    print(" Criar carrinho ".center(50, "="))
    pprint(requests.post(f"{URL}/cart/", json={
        "id": cart_id
    }).json())
    
    
    # Adicionar produto
    print("  Adicionar produto  ".center(50, "="))
    pprint(requests.post(f"{URL}/cart/add", params={
        "cart_id": cart_id,
        "product_id":3,
        "amount":2
    }).json())
    pprint(requests.post(f"{URL}/cart/add", params={
        "cart_id": cart_id,
        "product_id":4,
        "amount":1
    }).json())
    pprint(requests.post(f"{URL}/cart/add", params={
        "cart_id": cart_id,
        "product_id":5,
        "amount":2
    }).json())
    
    
    # Remover produto
    print("  Remover produto  ".center(50, "="))
    pprint(requests.post(f"{URL}/cart/remove", params={
        "cart_id": cart_id,
        "product_id":4,
        "amount":1
    }).json())
    
    
    # Aplicar deconto
    print("  Aplicar deconto  ".center(50, "="))
    pprint(requests.post(f"{URL}/salecart/{cart_id}/apply-coupon", params={
        "cart_id": cart_id,
        "coupon_code": "promo10" # Wrong coupon
    }).json())
    pprint(requests.post(f"{URL}/salecart/{cart_id}/apply-coupon", params={
        "cart_id": cart_id,
        "coupon_code": "OFERTA5" # Correct coupon
    }).json())
    
    
    # Finalizar compra
    print("  Finalizar compra  ".center(50, "="))
    pprint(requests.post(f"{URL}/checkout/{cart_id}", params={
        "payment_method": "pix"
    }).json())