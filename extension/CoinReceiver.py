from base.Receiver import Receiver
from extension.AllValues import CoinsValue


class CoinReceiver(Receiver):
    def process_input(self, instance):
        if self.__coin_authenticity_check():
            value = self.__define_coin_value(instance)
            self.machine.balance.add_money(value.value)
            self.machine.storage.add_money(value)
            self.machine.show_main_screen()
        else:
            self.__return_coin()

    def __define_coin_value(self, instance) -> CoinsValue:
        for value in CoinsValue:
            if float(instance.text) == value.value:
                return value

    def __coin_authenticity_check(self) -> bool:
        return True

    def __return_coin(self):
        pass
