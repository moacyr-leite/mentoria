import requests

URL = "http://127.0.0.1:8000"

def exibir_estoque():
    estoque = requests.get(f"{URL}/estoque/").json()

    print("Qual produto você gostaria de adicionar ao carrinho?")

    for i, produto in enumerate(estoque):
        print(f"{i}. {produto["nome"]}\n R$ {float(produto["preco"])/100}\n Quant. {produto["quantidade"]}")

    _in = int(input("\n"))
    if _in <= len(estoque)-1:
        produto_selecionado = estoque[_in]
        print(f"Produto adicionado ao carrinho: {produto_selecionado["nome"]}\n")


def main():
    while True:
        _in = input(f"\nO que gosaria de fazer?\n1. Comprar\n2. Exibir Carrinho\n3. Sair\n\n")
        match _in:
            case "1":
                exibir_estoque()
            case "2":
                return 
            case "3":
                return

if __name__ == "__main__":
    main()