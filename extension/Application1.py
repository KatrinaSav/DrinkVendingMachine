from base.Application import Application
from extension.DrinkVendingMachine1 import DrinkVendingMachine1
from extension.Storage import Storage
from extension.Balance1 import Balance1
from extension.BillReceiver import BillReceiver
from extension.CoinReceiver import CoinReceiver


class Application1(Application):

    def build(self):
        bill_receiver = BillReceiver()
        coin_receiver = CoinReceiver()
        storage = Storage()
        balance = Balance1()
        machine = DrinkVendingMachine1(bill_receiver, balance, coin_receiver, storage)
        bill_receiver.set_machine(machine)
        coin_receiver.set_machine(machine)
        return machine
