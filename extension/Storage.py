from typing import List
from extension.Cell import Cell
from extension.AllValues import *


class Storage:

    cells: List[Cell]

    def __init__(self):
        self.cells =[]
        for bill_value in BillsValue:
            self.cells.append(Cell(bill_value))
        for coin_value in CoinsValue:
            self.cells.append(Cell(coin_value))

    def add_money(self, value: Enum):
        for cell in self.cells:
            if value == cell.value:
                cell.add()
                break

    def define_change(self, value: float):
        current_value = value
        while current_value != 0:
            for cell in self.cells:
                if current_value >= cell.value.value and cell.number != 0:
                    current_value = round(current_value - cell.value.value, 2)
                    cell.take_away()

    def clear(self):
        for cell in self.cells:
            cell.number = 0
