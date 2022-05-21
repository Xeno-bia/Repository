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
from X import *            # ライブラリ(拡張)
class X:                   # クラス(設計図)
    def __init__(self, X): #   変数(情報)
    def X(self, X):        #   関数(機能)
X = X(X)                   # オブジェクト(物)
X.X                        #   変数(情報)
X.X(X)                     #   関数(機能)
'''