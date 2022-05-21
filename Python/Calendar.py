#----------#
# Calendar #
#----------#
from datetime import *
from calendar import *

class Calendar:
    def __init__(self):
        self.y = date.today().year
        self.m = date.today().month

    def this_month(self):
        setfirstweekday(6)
        print(month(self.y, self.m))

calendar = Calendar()
print(calendar.y)
calendar.this_month()

'''
from lib import *            # ライブラリ(拡張)

class Cls(sup):              # クラス(設計図)
    def __init__(self, arg): #   変数(情報)
    def func(self, arg):     #   関数(機能)

obj = Cls(arg)               # オブジェクト(物)
obj.var                      #   変数(情報)
obj.func(arg)                #   関数(機能)
'''