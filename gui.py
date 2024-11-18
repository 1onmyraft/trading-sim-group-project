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

        self.price_label = QLabel('')
        money_layout.add_widget(self.price_label)
       

        main_layout.add_layout(money_layout)

        trade_layout = QHBoxLayout()

        self.cryptos, self.crypto_ids = coingecko.get_coin_ids()
        
        self.crypto_combo = QComboBox()
        self.crypto_combo.add_items(self.cryptos)
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

       
        
      
    
app = QApplication([])
my_gui = Gui()
sys.exit(app.exec())
