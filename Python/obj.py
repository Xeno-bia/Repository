py       #インタプリタ起動
CTRL + C #インタプリタ終了
py x.py  #ファイル実行

#x #コメント

True, False #真偽値
x           #整数
x.x         #小数
f'x'        #文字列
[x]         #リスト
{x: x}      #辞書
x[x: x: x]  #抽出

bool(x)        #真偽値
int(x)         #整数
float(x)       #小数
str(x)         #文字列
list(x)        #リスト
dict(x)        #辞書
range(x, x, x) #連番

if x: #分岐
    x
elif x:
    x
else:
    x

x + x   #加算・連結
x - x   #減算
x * x   #乗算・繰り返し
x ** x  #冪乗
x / x   #除算
x // x  #整数除算
x % x   #剰余算
x == x  #等しい
x < x   #小なり
x <= x  #小なりイコール
x > x   #大なり
x >= x  #大なりイコール
x in x  #含む
x and x #かつ
x or x  #または
not x   #ではない

for i in x:  #コンテナループ
    x
    continue
    break
else:
    x
while x:     #条件ループ
    x
    continue
    break
else:
    x

def x(*x): #関数
    x
    return x

x(x)

class x(x): #クラス
    def __init__(self, *x):
        self.x = x

    def x(self, *x):
        x
        super().x(x)
        return x

x(x)
x.x
x.x(x)

from x import * #ライブラリ