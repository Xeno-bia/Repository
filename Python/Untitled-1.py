#1行

'''
複数行
'''

class Cls:
    def __init__(self, arg):
        self.var = ...

    def method(self, arg):
        ...
        return ...

Cls = Cls(arg)

Cls.var

Cls.func(arg)

'''
with open('txt.txt', mode='w', encoding='utf-8') as var: #ファイルを作成・上書き
    var.write('')

with open('txt.txt', mode='a', encoding='utf-8') as var: #ファイルに追記
    var.write('')
'''

with open('txt.txt', mode='r', encoding='utf-8') as var: #ファイルを取得
    var.read()

#pip list               #ライブラリ一覧
#pip install lib        #ライブラリインストール
#pip install pip-review #ライブラリアップデート
#pip-review -a

from playsound import *
playsound('mp3.mp3') #MP3を再生

from webbrowser import *
open('url') #Webサイトを開く

list()[start: stop] #取得
list().append(x)       #追加
list().count(x)        #出現数
list().extend(list)       #連結
list().index()        #位置
list().insert(x)       #追加
del x          #削除
list().reverse()      #反転
list().sort()         #並べ替え

set().add(x) #追加
del x               #削除
set().update(set) #連結

dict()[key] #値を取得
dict().keys()#キーリスト
dict().values()#値リスト
dict().items() #キー・値リスト
del x #削除
dict().update() #連結

#エスケープ
'\a'             #アラート
'\\'             #バックスラッシュ
'\''             #クォート
'\b'             #バックスペース
'\t'             #タブ
'\n'             #改行
'\f'             #改ページ

'''
#pattern_matching
match object:
    case pattern:
        pass
    case _:
        pass
'''

#ランダム
from random import *
randint(start, stop) #乱数
choice(ctn) #選択

#時間
from time import *
sleep(sec) #待機

#整形出力
from pprint import *
pprint(x) #整形出力

#分数
from fractions import *
Fraction(x, y) #分数

#数学
from math import *
pi                  #円周率
inf                 #無限大
log(x, y)           #対数
sin(a)              #正弦
cos(a)              #余弦
tan(a)              #正接

#日時
from datetime import *
datetime.now(),                                                              #現在の日時
date.today(),                                                                #今日の日付
datetime(year, month, day, hour, minute, second),                            #日時
date(year, month, day),                                                      #日付
time(hour, minute, second),                                                  #時刻
timedelta(weeks=week, days=day, hours=hour, minutes=minute, seconds=second), #日時差

#カレンダー
from calendar import *
calendar(year)     #年間カレンダー
month(year, month) #月間カレンダー

#ログ
from logging import basicConfig,DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical
basicConfig(filename=file,level=level,format=format)
debug(メッセージ)
info(メッセージ)
warning(メッセージ)
error(メッセージ)
critical(メッセージ)

'''
os
sympy
Numpy
itertools
statistics
janome.tokenizer(Tokenizer, .tokenize, .surface)
openpyxl
'''

#システム
from sys import *
argv #コマンドライン引数

#分岐
if ...:
    ...
elif ...:
    ...
else:
    ...

#コンテナループ
for var in ctn:
    ...
    if ...:
        continue
    if ...:
        break
else:
    ...

#条件ループ
while ...:
    ...
    if ...:
        continue
    if ...:
        break
else:
    ...

#例外送出
raise exp('msg')

#例外処理
try:
    ...
except exp:
    ...
else:
    ...
finally:
    ...
