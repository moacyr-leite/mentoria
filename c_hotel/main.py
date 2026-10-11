from fastapi import FastAPI
from pydantic import BaseModel

import json

class Reservation(BaseModel):
    week: int
    weekend: int
    userType: str

class Price(BaseModel):
    week: int
    weekend: int

class GuidePrice(BaseModel):
    single: Price
    premium: Price

class Hotel(BaseModel):
    name: str
    stars: int
    price: GuidePrice

app = FastAPI()

def read_data(file_name) -> list:
    data = []
    with open(f"{file_name}.json", "r", encoding="utf-8") as f_data:
        data = json.load(f_data)
    return data

def white_data(file_name, data):
    with open(f"{file_name}.json", "w", encoding="utf-8") as f_data:
        json.dump(data, f_data, indent=4, ensure_ascii=False)

@app.get("/hotel/")
async def get_hotels():
    return read_data("hotel")

@app.post("/hotels/")
async def create_hotel(hotel: Hotel):
    file_name = "hotel"
    data = read_data(file_name)
    data.append(hotel.model_dump())
    white_data(file_name, data)

    return True

@app.post("/")
async def hotel_price_for_reservation(reservation: Reservation):
    hotels = read_data("hotel")
    result = []
    for h in hotels:
        hotel = Hotel(**h)
        price:Price = hotel.price.__getattribute__(reservation.userType)
        p_week = price.week * reservation.week
        p_weekend = price.weekend * reservation.weekend
        result.append({
            "hotel": hotel.name,
            "stars": hotel.stars,
            "totalPrice": p_week + p_weekend
        })

    return result