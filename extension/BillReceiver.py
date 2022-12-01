from base.Receiver import Receiver
from extension.AllValues import BillsValue


class BillReceiver(Receiver):

    def process_input(self, instance):
        if self.__bill_authenticity_check():
            value = self.__define_bill_value(instance)
            self.machine.balance.add_money(value.value)
            self.machine.storage.add_money(value)
            self.machine.show_main_screen()
        else:
            self.__return_bill()

    def __define_bill_value(self, instance) -> BillsValue:
        for value in BillsValue:
            if float(instance.text) == value.value:
                return value

    def __bill_authenticity_check(self) -> bool:
        return True

    def __return_bill(self):
        pass
