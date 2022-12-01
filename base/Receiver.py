class Receiver:

    machine: 'DrinksVendingMachine'

    def set_machine(self, machine: 'DrinksVendingMachine'):
        self.machine = machine

    def process_input(self, instance):
        self.machine.balance.add_money(int(instance.text))
        self.machine.show_main_screen()
        instance.text = ""
