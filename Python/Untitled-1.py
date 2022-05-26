'''
コマンド
コメント
ライブラリ
リテラル
演算子
文
変数・関数
クラス(フィールド・メソッド)
'''
#----------#
# コマンド #
#----------#
'''
$ pip list
$ pip install lib
$ pip-review --auto
$ py xxx.py
$ pyinstaller xxx.py --onefile --noconsole --icon=img
'''

#----------#
# コメント #
#----------#
# cmt

#------------#
# ライブラリ #
#------------#
from lib import *

#----------#
# リテラル #
#----------#
int
flt
'str'
[val]
{key: val}

#--------#
# 演算子 #
#--------#
x + y
x - y
x * y
x ** y
x / y
x // y
x % y
x == y
x < y
x <= y
x > y
x >= y
x in y
x and y
x or y
not x

#----#
# 文 #
#----#
return rtn

if con:
    xxx
elif con:
    xxx
else:
    xxx

for i in ctn:
    xxx
    continue
    break

while con:
    xxx
    continue
    break

with file as var:
    xxx

raise exc(msg)

try:
    xxx
except exc:
    xxx
else:
    xxx

#------------#
# 変数・関数 #
#------------#
var = xxx
def func(arg):
    xxx
var
func(arg)

#------------------------------#
# クラス(フィールド・メソッド) #
#------------------------------#
class Cls(sup):
    fld = xxx
    def meth(self, arg):
        xxx
obj = Cls(arg)
obj.fld
obj.meth(arg)