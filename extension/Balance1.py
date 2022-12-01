from base.Balance import Balance


class Balance1(Balance):

    def __init__(self):
        super().__init__()

    def reset(self):
        self.deposited_money = 0
