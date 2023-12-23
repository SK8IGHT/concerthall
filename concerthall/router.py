from fastapi import APIRouter 
from pydantic import BaseModel  
from typing import List  
import sqlite3  

router = APIRouter() 

concert_id: int
venue_id: int
artist: str
date: str
ticket_price: int


@router.get("/concerts", response_model=List[Concert])
def get_concerts():
    conn = sqlite3.connect('database.db')  
    cursor = conn.cursor()  


    cursor.execute('SELECT * FROM Concert')
    concerts = cursor.fetchall() 

    conn.close() 


    concert_list = []
    for concert in concerts:
        concert_obj = Concert(
            concert_id=concert[0],
            venue_id=concert[1],
            artist=concert[2],
            date=concert[3],
            ticket_price=concert[4]
        )
        concert_list.append(concert_obj)

    return concert_list