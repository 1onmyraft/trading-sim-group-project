from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator, QPixmap
from __feature__ import snake_case, true_property
import sys

import coingecko

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.window_title = 'Trade Simy'

        #To add image
        # label = QLabel()
        # my_pixmap = QPixmap('images/crypto-image.jpg')
        # my_pixmap = my_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        # label.pixmap = my_pixmap
        # self.layout = QVBoxLayout()
        # self.layout.add_widget(label)
        # self.set_layout(self.layout)




        main_layout = QVBoxLayout()

        money_layout = QHBoxLayout()
        self.money = float(100000.00) # if saving you should load from file
        self.money_label = QLabel('$' + str(self.money))
        money_layout.add_widget(QLabel('Balance:'))
        money_layout.add_widget(self.money_label)

        money_layout.add_widget(QLabel(' ')) # spacing

        self.price_label = QLabel('')#$' + str('1000') + ' per coin')

        price_layout = QVBoxLayout()

        price_layout.add_widget(self.price_label)

        self.worth_label = QLabel('')

        price_layout.add_widget(self.worth_label)

        
        money_layout.add_layout(price_layout)

        

        
       

        main_layout.add_layout(money_layout)

        main_layout.add_widget(QLabel('Select a Coin:'))

        trade_layout = QHBoxLayout()

        self.cryptos, self.crypto_ids = coingecko.get_coin_ids()

        self.owned_cryptos = {} # in coin value not usd

        for c in self.cryptos: # should load from file if saving
            self.owned_cryptos[c] = 0
            
        
        self.crypto_combo = QComboBox()
        self.crypto_combo.add_items(self.cryptos)

        self.crypto_combo.currentIndexChanged.connect(self.combo_changed)
        
        trade_layout.add_widget(self.crypto_combo)
        

        main_layout.add_layout(trade_layout)

        buttons_layout = QHBoxLayout()
        buy_button = QPushButton('Buy')
        buy_button.clicked.connect(self.buy_btn)
        sell_button = QPushButton('Sell')
        sell_button.clicked.connect(self.sell_btn)

        view_button = QPushButton('View image for currency')
        view_button.clicked.connect(self.view_btn)

        self.amount_box = QLineEdit()
        self.amount_box.placeholder_text = 'Enter Amount'

        only_float = QDoubleValidator()
        only_float.set_range(0, 1000000)
        self.amount_box.set_validator(only_float)
        self.amount_box.textChanged.connect(self.box_changed)

        buttons_layout.add_widget(buy_button)
        buttons_layout.add_widget(sell_button)
        buttons_layout.add_widget(view_button)

        amount_layout = QVBoxLayout()
        amount_layout.add_widget(self.amount_box)
        self.amount_label = QLabel('')
        amount_layout.add_widget(self.amount_label)
        buttons_layout.add_layout(amount_layout)

        main_layout.add_layout(buttons_layout)    

        self.set_layout(main_layout)

        self.combo_changed()
        self.resize(400, 200)
        self.show()

    def get_price(self, coin_name):
        coin_id = ''
        
        
        for idx, c_name in enumerate(self.cryptos) :
            if c_name == coin_name:
                coin_id = self.crypto_ids[idx]
            
            
        price = coingecko.get_price(coin_id)
        return price

    def update(self):
        self.money_label.text = '$' + str(round(self.money, 2))
        self.combo_changed()

    def box_changed(self):
        if self.amount_box.text == '':
            self.amount_label.text = ''
            return
        
        coin_name = self.crypto_combo.current_text
        price = self.get_price(coin_name)
        amount = float(self.amount_box.text)
        
        self.amount_label.text = '$' + str(round(price * amount, 2))
        

    def combo_changed(self):
        coin_name = self.crypto_combo.current_text
        price = self.get_price(coin_name)
        self.price_label.text = 'Owned '+str(round(self.owned_cryptos[coin_name], 2)) +'. Current price: $' + str(round(price, 2))
        self.worth_label.text = 'Worth $' + str(round(price * self.owned_cryptos[coin_name], 2))

    def buy(self, coin_name, amount):
        price = self.get_price(coin_name)
        if self.money >= price * amount:
            self.money -= price*amount

            self.owned_cryptos[coin_name] += amount
        
        
    def sell(self, coin_name, amount):
        price = self.get_price(coin_name)
        if self.owned_cryptos[coin_name] >= amount:
            self.money += price*amount

            self.owned_cryptos[coin_name] -= amount

    def buy_btn(self):
        coin_name = self.crypto_combo.current_text
        amount = float(self.amount_box.text)
        self.buy(coin_name, amount)
        self.update()
        

    def sell_btn(self):
        coin_name = self.crypto_combo.current_text
        amount = float(self.amount_box.text)
        self.sell(coin_name, amount)
        self.update()
      
    def view_btn(self):
        self.new_win = NewWindow()
        self.new_win.show()


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        my_pixmap = QPixmap('images/crypto-image.jpg')
        label.pixmap = my_pixmap
        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        self.set_layout(self.layout)




app = QApplication([])
my_gui = Gui()
sys.exit(app.exec())
