from Balance import Balance
from Receiver import Receiver
from DrinkVendingMachine import DrinksVendingMachine


class Application:

    def build(self) -> DrinksVendingMachine:
        receiver = Receiver()
        balance = Balance()
        machine = DrinksVendingMachine(receiver, balance)
        receiver.set_machine(machine)
        return machine

    def main(self):
        self.build().run()
