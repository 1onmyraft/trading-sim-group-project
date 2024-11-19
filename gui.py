from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property
import sys

import coingecko

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.window_title = 'Trade Sim'

        
        main_layout = QVBoxLayout()

        money_layout = QHBoxLayout()
        self.money = 100000
        self.money_label = QLabel('$' + str(self.money))
        money_layout.add_widget(self.money_label)

        money_layout.add_widget(QLabel(' ')) # spacing

        self.price_label = QLabel('')#$' + str('1000') + ' per coin')
        money_layout.add_widget(self.price_label)

        

        
       

        main_layout.add_layout(money_layout)

        main_layout.add_widget(QLabel('Select a Coin:'))

        trade_layout = QHBoxLayout()

        self.cryptos, self.crypto_ids = coingecko.get_coin_ids()
        
        self.crypto_combo = QComboBox()
        self.crypto_combo.add_items(self.cryptos)

        self.crypto_combo.currentIndexChanged.connect(self.combo_changed)
        
        trade_layout.add_widget(self.crypto_combo)
        

        main_layout.add_layout(trade_layout)

        buttons_layout = QHBoxLayout()
        buy_button = QPushButton('Buy')
        sell_button = QPushButton('Sell')

        buttons_layout.add_widget(buy_button)
        buttons_layout.add_widget(sell_button)

        main_layout.add_layout(buttons_layout)    

        self.set_layout(main_layout)

        self.show()

    def combo_changed(self):
        coin_name = self.crypto_combo.current_text
        coin_id = ''
        for idx, c_name in enumerate(self.cryptos) :
            if c_name == coin_name:
                coin_id = self.crypto_ids[idx]
            
        price = coingecko.get_price(coin_id)
        self.price_label.text = '$' + str(price)
       
        
      
    
app = QApplication([])
my_gui = Gui()
sys.exit(app.exec())
