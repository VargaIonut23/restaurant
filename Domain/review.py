from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class review(Entity):
    numeclient: str
    idrestaurant: str
    comentariu: str
    nota: int
