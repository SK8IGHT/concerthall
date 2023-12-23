from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Venue(BaseModelModify):
    name: str
    capacity: int
    location: str
    phone: str


class Concert(BaseModelModify):
    venue_id: int
    artist: str
    date: datetime
    ticket_price: float


class Ticket(BaseModelModify):
    concert_id: int
    seat_number: int
    is_sold: bool


class Band(BaseModelModify):
    name: str
    genre: str
    formed_year: int


class Musician(BaseModelModify):
    band_id: int
    name: str
    instrument: str


class Attendee(BaseModelModify):
    name: str
    email: str


class TicketSale(BaseModelModify):
    ticket_id: int
    attendee_id: int
    sale_date: datetime


class Review(BaseModelModify):
    concert_id: int
    attendee_id: int
    rating: int
    comment: str


class ArtistSchedule(BaseModelModify):
    artist: str
    date: datetime
    venue_id: int


class EventStaff(BaseModelModify):
    name: str
    role: str
    venue_id: int


class Sponsor(BaseModelModify):
    name: str
    logo_url: str


class ConcertSponsorship(BaseModelModify):
    concert_id: int
    sponsor_id: int
