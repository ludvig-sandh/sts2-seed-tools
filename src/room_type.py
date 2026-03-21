from enum import Enum


class RoomType(Enum):
    UNASSIGNED = 0
    MONSTER = 1
    ELITE = 2
    BOSS = 3
    TREASURE = 4
    SHOP = 5
    EVENT = 6
    RESTSITE = 7
    MAP = 8