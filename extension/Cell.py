from enum import Enum


class Cell:

    number: int
    value: Enum

    def __init__(self, value: Enum):
        self.number = 0
        self.value = value

    def take_away(self):
        self.number -= 1

    def add(self):
        self.number += 1
