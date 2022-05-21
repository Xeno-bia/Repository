print('''
from calendar import *                        # 拡張機能calendarを使用
from datetime import *                        # 拡張機能datetimeを使用

class Calendar:                               # カレンダーオブジェクトを作成
    def this_month(self):                     # → 今月のカレンダー表示機能を作成
        setfirstweekday(6)                    # → → 今月の開始曜日を設定
        self.today = date.today()             # → → 今日の日付を取得
        self.year = self.today.year           # → → 今日の年を取得
        self.month = self.today.month         # → → 今日の月を取得
        self.x = month(self.year, self.month) # → → カレンダーを作成
        print(self.x)                         # → → カレンダーを表示

calendar = Calendar()                         # カレンダーオブジェクトを取得
calendar.this_month()                         # 今月のカレンダー表示機能を使用
''')

from calendar import *                        # 拡張機能calendarを使用
from datetime import *                        # 拡張機能datetimeを使用

class Calendar:                               # カレンダーオブジェクトを作成
    def this_month(self):                     # → 今月のカレンダー表示機能を作成
        setfirstweekday(6)                    # → → 今月の開始曜日を設定
        self.today = date.today()             # → → 今日の日付を取得
        self.year = self.today.year           # → → 今日の年を取得
        self.month = self.today.month         # → → 今日の月を取得
        self.x = month(self.year, self.month) # → → カレンダーを作成
        print(self.x)                         # → → カレンダーを表示

calendar = Calendar()                         # カレンダーオブジェクトを取得
calendar.this_month()                         # 今月のカレンダー表示機能を使用