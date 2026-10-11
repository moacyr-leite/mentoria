"""
    dados:
    1. Hotel Aurora Palace ⭐⭐⭐
    Regular:
    Semana: R$ 110
    Final de semana: R$ 90
    Premium:
    Semana: R$ 80
    Final de semana: R$ 80

    2. Hotel Costa Verde Resort ⭐⭐⭐⭐
    Regular:
    Semana: R$ 160
    Final de semana: R$ 60
    Premium:
    Semana: R$ 110
    Final de semana: R$ 50

    3. Hotel Imperial Prime ⭐⭐⭐⭐⭐
    Regular:
    Semana: R$ 220
    Final de semana: R$ 150
    Premium:
    Semana: R$ 100
    Final de semana: R$ 40
"""

"""
    output:
    [
    {
        "hotel": "Hotel Aurora Palace",
        "stars": 3,
        "totalPrice": 240
    },
    {
        "hotel": "Hotel Costa Verde Resort",
        "stars": 4,
        "totalPrice": 270
    },
    {
        "hotel": "Hotel Imperial Prime",
        "stars": 5,
        "totalPrice": 240
    }
    ]
"""

"""
    input:
    {
    "dates": ["2026-03-13", "2026-03-14", "2026-03-15"],
    "userType": "premium"
    }
"""

from datetime import datetime
from hotel import Hotel
import requests

def date_helper(list_dates):
    dates = {
        "week": 0,
        "weekend": 0
    }
    for date in list_dates:
        d = datetime.fromisoformat(date).weekday()
        if d in [5,6]:
            dates["weekend"] += 1
        else:
            dates["week"] += 1

    return dates
            
def main():
    hotel_1 = Hotel("Hotel Aurara Palace", 3, {
        "regular": {
            "semana": 110,
            "fim_semana": 90
        },
        "premium": {
            "semana": 80,
            "fim_semana": 80
        }
    })
    hotel_2 = Hotel("Hotel Costa Verde Resort", 4, {
        "regular": {
            "semana": 160,
            "fim_semana": 60
        },
        "premium": {
            "semana": 110,
            "fim_semana": 50
        }
    })
    hotel_3 = Hotel("Hotel Imperial Prime", 5, {
        "regular": {
            "semana": 220,
            "fim_semana": 150
        },
        "premium": {
            "semana": 100,
            "fim_semana": 40
        }
    })

    input= {
        "dates": ["2026-03-13", "2026-03-14", "2026-03-15"],
        "userType": "premium"
    }

    output = []

    dates = {
        "semana": 0,
        "fim_semana": 0
    }

    for date in input["dates"]:
        d = datetime.fromisoformat(date).weekday()
        if d in [5,6]:
            dates["fim_semana"] += 1
        else:
            dates["semana"] += 1

    for hotel in [hotel_1, hotel_2, hotel_3]:
        output.append(
            {
                "hotel": hotel.nome,
                "stars": hotel.star,
                "totalPrice": hotel.price_estadia(dates, input["userType"])
            }
        )
    print(output)

def main_api():
    input= {
        "dates": ["2026-03-13", "2026-03-14", "2026-03-15"],
        "userType": "premium"
    }

    days_week = date_helper(input["dates"])
    days_week.update({"userType":input["userType"]})

    r = requests.post("http://127.0.0.1:8000/", json=days_week)
    print(r.status_code)
    print(r.json())

if __name__ == "__main__":
    #main()
    main_api()

# Criar API
# ordenar "filter"

"""
pesquisar:
flask
fastapi

"""