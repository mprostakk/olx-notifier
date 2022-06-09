from dataclasses import dataclass


@dataclass
class Offer:
    title: str
    promoted: bool
    price: str
    link: str
    is_today: bool
