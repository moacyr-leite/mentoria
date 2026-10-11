
class Hotel:
    """
    nome: string
    star: int
    price: dict
    {
        "regular": {
            "semana": 0,
            "fim_semana: 0
        },
        "premium": {
            "semana": 0,
            "fim_semana: 0
        }
    }
    """
    
    def __init__(self, nome:str, star:int, price:dict):
        self.nome = nome
        self.star = star
        self.price = price

    def price_estadia(self, dates:list[str], userType:str):
        """
        dates: {
            "semana": 0,
            "fim_semana": 0
        }
        """

        price_user = self.price.get(userType)
        
        price_semana = price_user.get("semana") * dates["semana"]
        price_fim_semana = price_user.get("fim_semana") * dates["fim_semana"]

        return price_semana + price_fim_semana