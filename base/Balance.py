class Balance:

    deposited_money: float

    def __init__(self):
        self.deposited_money = 0

    def add_money(self, value: float):
        self.deposited_money += value
        self.deposited_money = round(self.deposited_money, 2)

    def take_away_money(self, amount: float):
        pass
