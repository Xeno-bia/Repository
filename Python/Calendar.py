'''
from X import *            #拡張
class X:                   #クラス
    def __init__(self, X): #情報
    def X(self, X):        #機能
X = X(X)                   #オブジェクト
X.X                        #情報
X.X(X)                     #機能
'''

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
calendar.this_month()