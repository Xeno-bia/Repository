from calendar import *                        #calendarライブラリを呼び出し
from datetime import *                        #datetimeライブラリを呼び出し

class Calendar:                               #カレンダーオブジェクトを作成
    def this_month(self):                     #今月のカレンダー表示機能を作成
        setfirstweekday(6)                    #週の開始曜日を変更
        self.today = date.today()             #現在の日付を呼び出し
        self.year = self.today.year           #現在の年を呼び出し
        self.month = self.today.month         #現在の月を呼び出し
        self.x = month(self.year, self.month) #今月のカレンダーを作成
        print(self.x)                         #今月のカレンダーを表示

calendar = Calendar()                         #カレンダーオブジェクトを呼び出し
calendar.this_month()                         #今月のカレンダー表示機能を呼び出し