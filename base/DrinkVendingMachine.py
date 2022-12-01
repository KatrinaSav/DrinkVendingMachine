from Balance import Balance
from Receiver import Receiver
from MachineStates import MachineStates
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class DrinksVendingMachine(App):

    state: MachineStates
    balance: Balance
    receiver: Receiver

    def __init__(self, receiver: Receiver, balance: Balance, **kwargs):
        super().__init__(**kwargs)
        self.balance = balance
        self.receiver = receiver
        self.state = MachineStates.drink_sale

    def build(self):
        root = Builder.load_file('view.kv')
        return root

    def set_receiver(self, receiver: Receiver):
        self.receiver = receiver

    def set_balance(self, balance: Balance):
        self.balance = balance

    def show_main_screen(self):
        self.root.current = 'Main'
        box = self.root.ids.main_screen.ids.screen1
        box.clear_widgets(children=None)
        box.add_widget(Button(text='Перевести в режим обслуживания', on_press=self.on_transfer_to_service))
        box.add_widget(Button(text='Выбрать напиток', on_press=self.on_drink_choosen))
        box.add_widget(Label(text="Баланс:" + str(self.balance.deposited_money)))
        box.add_widget(TextInput(text='', multiline=False))
        box.add_widget(Button(text='Внести деньги', on_press=self.receiver.process_input))

    def show_ready_drink_screen(self):
        pass

    def show_service_screen(self):
        self.root.current = 'Service'
        box = self.root.ids.service_screen.ids.screen2
        box.clear_widgets(children=None)
        box.add_widget(Button(text='Перевести в режим продажи', on_press=self.on_complite_service))

    def on_transfer_to_service(self, instance):
        self.state = MachineStates.service_maintenance
        self.show_service_screen()

    def on_complite_service(self, instance):
        self.state = MachineStates.drink_sale
        self.show_main_screen()

    def on_drink_choosen(self, name: str):
        pass

    class MainScreen(Screen):
        pass

    class ServiceScreen(Screen):
        pass
