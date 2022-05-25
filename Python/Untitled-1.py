'''
ライブラリ
変数・関数
オブジェクト(フィールド・メソッド)
'''

# コマンド
'''
$ pip list                                            # ライブラリ一覧
$ pip install lib                                     # ライブラリインストール
$ pip-review --auto                                   # ライブラリアップデート
$ py xxx.py                                           # 実行
$ pyinstaller xxx.py --onefile --noconsole --icon=img # EXE化
'''
#------------#
# ライブラリ #
#------------#
from lib import * # ライブラリ呼び出し

#------------#
# 変数・関数 #
#------------#
var = xxx      # 変数作成
var            # 変数呼び出し

def func(arg): # 関数作成
    xxx
    return rtn
func(arg)      # 関数呼び出し

#------------------------------------#
# オブジェクト(フィールド・メソッド) #
#------------------------------------#
class Cls(sup):          # クラス作成
    fld = xxx            # フィールド作成
    def meth(self, arg): # メソッド作成
        xxx
        return rtn
obj = Cls(arg)           # オブジェクト作成
obj.fld                  # フィールド呼び出し
obj.meth(arg)            # メソッド呼び出し

a.append(b)          # 追加
a.remove(b)          # 削除
a.sort()             # 昇順
a.sort(reverse=True) # 降順

from builtins import *              # 組み込みライブラリ
builtins.print(xxx, sep=sep) #     出力関数
builtins.input(msg)          #     入力関数
builtins.max(ctn)            #     最大値関数
builtins.min(ctn)            #     最小値関数
builtins.sum(ctn)            #     合計関数

int = builtins.int(num)      #     整数オブジェクト
int.__add__(num)             #         加算メソッド
int.__sub__(num)             #         減算メソッド
int.__mul__(num)             #         乗算メソッド
int.__pow__(num)             #         冪乗メソッド
int.__truediv__(num)         #         除算メソッド
int.__divmod__(num)          #         剰余算メソッド
int.__eq__(num)              #         等価メソッド
int.__lt__(num)              #         未満メソッド
int.__le__(num)              #         以下メソッド
int.__gt__(num)              #         超過メソッド
int.__ge__(num)              #         以上メソッド
int.__and__()

float = builtins.float(num)  #     小数オブジェクト
float.__add__(num)           #         加算メソッド
float.__sub__(num)           #         減算メソッド
float.__mul__(num)           #         乗算メソッド
float.__pow__(num)           #         冪乗メソッド
float.__truediv__(num)       #         除算メソッド
float.__divmod__(num)        #         剰余算メソッド
float.__eq__(num)            #         等価メソッド
float.__lt__(num)            #         未満メソッド
float.__le__(num)            #         以下メソッド
float.__gt__(num)            #         超過メソッド
float.__ge__(num)            #         以上メソッド

str = builtins.str('str')    #     文字列オブジェクト
str.count(str)               #         個数メソッド
str.replace(old, new)        #         置換メソッド
str.split(sep)               #         分割メソッド
str.__len__()                #         長さメソッド

builtins.list(xxx)           #     リストオブジェクト
builtins.set(xxx)            #     集合オブジェクト
builtins.dict(xxx)           #     辞書オブジェクト
builtins.range(b, e, s)      #     連番オブジェクト

# 演算子
x in y  # 包含

# 文
with file as var: # ファイル
    xxx

if con:           # 分岐
    xxx
elif con:
    xxx
else:
    xxx

for i in ctn:     # コンテナループ
    xxx
    continue      # スキップ
    break         # 終了

while con:        # 条件ループ
    xxx
    continue      # スキップ
    break         # 終了

raise exc(msg)    # 例外送出

try:              # 例外処理
    xxx
except exc:
    xxx
else:
    xxx