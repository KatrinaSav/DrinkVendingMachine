from extension.CoinReceiver import CoinReceiver
from extension.BillReceiver import BillReceiver
from base.DrinkVendingMachine import DrinksVendingMachine
from extension.Balance1 import Balance1
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class DrinkVendingMachine1(DrinksVendingMachine):

    coin_receiver: CoinReceiver

    def __init__(self, receiver: BillReceiver, balance: Balance1, coin_receiver: CoinReceiver, **kwargs):
        super().__init__(receiver, balance, **kwargs)
        self.coin_receiver = coin_receiver

    def show_main_screen(self):
        self.root.current = 'Main'
        box = self.root.ids.main_screen.ids.screen1
        box.clear_widgets(children=None)
        box.add_widget(Button(text='Перевести в режим обслуживания', on_press=self.on_transfer_to_service))
        box.add_widget(Button(text='Выбрать напиток', on_press=self.on_drink_choosen))
        box.add_widget(Button(text='Забрать сдачу', on_press=self.on_take_change))
        box.add_widget(Label(text="Баланс:" + str(self.balance.deposited_money)))
        box.add_widget(TextInput(text='Внесите купюру', on_text_validate=self.receiver.process_input, multiline=False))
        box.add_widget(TextInput(text='Внесите монету', on_text_validate=self.coin_receiver.process_input,
                                 multiline=False))

    def show_service_screen(self):
        super().show_service_screen()
        box = self.root.ids.service_screen.ids.screen2
        box.add_widget(Button(text="Очистить хранилище", on_press=self.on_take_accumulated_money))

    def on_take_accumulated_money(self, instance):
        self.receiver.storage.clear()
        self.__give_money()

    def on_take_change(self, instance):
        self.receiver.storage.define_change(self.balance.deposited_money)
        self.__give_money()
        self.balance.reset()
        self.show_main_screen()

    def __give_money(self):
        pass
