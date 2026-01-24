from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title = "Sleeper Bus Booking API")

# mock database in memory
stations = [
    "Ahmedabad",
    "Vadodara",
    "Surat",
    "Vapi",
    "Mumbai"
] 

seats = [f"L{i}" for i in range(1, 12)] + [f"U{i}" for i in range(1, 12)]
meals = ["Veg", "Jain", "Snacks"]
bookings ={}

# schema for booking request

class SeatBookingRequest(BaseModel):
    seat_number : str
    from_station : str
    to_station : str

class MealBookingRequest(BaseModel):
    booking_id : str
    meal_type : str
    
class CancleBookingRequest(BaseModel):
    booking_id : str


# Helper Function

def is_seat_available(seat_number, from_station, to_station):
    for booking in booking.value():
        if booking["seat_number"] == seat_number:
            if not(
                stations.index(to_station) <= stations.index(booking["from_station"]) or
                stations.index(from_station) >= stations.index(booking["to_station"])
            ):
                return False
    return True


# APIs [Endpoints]

@app.get("/stations")
def get_stations():
    return {"stations": stations}

@app.get("/seats")
def list_seats(from_station: str, to_station: str):
    available = [
        seat for seat in seats if is_seat_available(seat, from_station, to_station)
    ]
    return {
        "available_seats": available,
        "total_available": len(available)
    }

@app.post("/book_seat")
def book_seat(request: SeatBookingRequest):
    if request.seat_number not in seats:
        raise HTTPException(status_code = 400, detail="Invalid seat number")

    if not is_seat_available(request.seat_number, request.from_station, request.to_station):
        raise HTTPException(status_code =400 , detail ="Seat not available")
    
    booking_id = str(uuid.uuid4())
    bookings[booking_id] = {
        "seat_number" : request.seat_number,
        "from_station": request.from_station,
        "to_station": request.to_station,
        "meal": None,
        "status": "CONFIRMED"
    }

    return {
        "message": "Seat booked successfully",
        "booking_id": booking_id
    }

@app.post("/book_meal")
def book_meal(request: MealBookingRequest):
    if request.booking_id not in bookings:
        raise HTTPException(status_code=400, detail="Booking not found")
    if request.meal_type not in meals:
        raise HTTPException(status_code = 400,detail="Invalid meal type")
    
    bookings[request.booking_id]["meal"] = request.meal_type
    return{
        "message": "meal added successfully",
        "booking_details": request.booking_id,
        "meal": request.meal_type
    }

@app.post("/cancel_booking")
def cancel_booking(request: CancleBookingRequest):
    if request.booking_id not in bookings:
        raise HTTPException(status_code=400, detail="Booking not found")
    
    bookings[request.booking_id]["status"] = "CANCELLED"

    return{
        "message": "Booking cancelled successfully",
        "booking_id": request.booking_id
    }
