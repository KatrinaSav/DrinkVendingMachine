from enum import Enum


class BillsValue(Enum):
    hundred = 100
    fifty = 50
    twenty = 20
    ten = 10
    five = 5


class CoinsValue(Enum):
    two = 2
    one = 1
    fifty_copeck = 0.5
    twenty_copeck = 0.2
    ten_copeck = 0.1
    five_copeck = 0.05
    two_copeck = 0.02
    copeck = 0.01
