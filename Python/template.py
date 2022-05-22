# comment                         # コメント

# 拡張
from library import *             # ライブラリ

# クラス
class Class(super):               # クラス
    def __init__(self, argument): # 変数
        pass
    def method(self, argument):   # メソッド
        pass

instance = Class(argument)        # インスタンス
instance.variable                 # 変数
instance.method(argument)         # メソッド

# 型
True, False                       # 真偽値
0                                 # 整数
0.0                               # 小数
range(start, stop, step)          # 連番
f'string'                         # 文字列
[value]                           # 配列
{key: value}                      # 辞書
container[start: stop: step]      # 抽出

# 演算子
x + x                             # 加算・連結
x - x                             # 減算
x * x                             # 乗算・繰り返し
x ** x                            # 冪乗
x / x                             # 除算
x // x                            # 整数除算
x % x                             # 剰余算
x == x                            # 等価
x < x                             # 未満
x <= x                            # 以下
x > x                             # 超過
x >= x                            # 以上
x in x                            # 包含
x and x                           # 論理積
x or x                            # 論理和
not x                             # 論路否定

# 制御
if condition:                     # 分岐
    pass
elif condition:
    pass
else:
    pass

for variable in container:        # コンテナループ
    pass
    continue
    break

while condition:                  # 条件ループ
    pass
    continue
    break

# > py program.py                 # 実行