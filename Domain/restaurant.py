from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class restaurant(Entity):
    nume: str
    adresa: str
    vegetarian: bool
