print('''
from calendar import *                        # 拡張機能calendar使用
from datetime import *                        # 拡張機能datetime使用

class Calendar:                               # カレンダーオブジェクト作成
    def this_month(self):                     # → 今月のカレンダー表示機能作成
        setfirstweekday(6)                    # → → 開始曜日設定
        self.today = date.today()             # → → 今日取得
        self.year = self.today.year           # → → 今年取得
        self.month = self.today.month         # → → 今月取得
        self.x = month(self.year, self.month) # → → カレンダー作成
        print(self.x)                         # → → カレンダー表示

calendar = Calendar()                         # カレンダーオブジェクト取得
calendar.this_month()                         # 今月のカレンダー表示機能使用
''')

from calendar import *                        # 拡張機能calendar使用
from datetime import *                        # 拡張機能datetime使用

class Calendar:                               # カレンダーオブジェクト作成
    def this_month(self):                     # → 今月のカレンダー表示機能作成
        setfirstweekday(6)                    # → → 開始曜日設定
        self.today = date.today()             # → → 今日取得
        self.year = self.today.year           # → → 今年取得
        self.month = self.today.month         # → → 今月取得
        self.x = month(self.year, self.month) # → → カレンダー作成
        print(self.x)                         # → → カレンダー表示

calendar = Calendar()                         # カレンダーオブジェクト取得
calendar.this_month()                         # 今月のカレンダー表示機能使用