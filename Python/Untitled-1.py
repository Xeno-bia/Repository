$ pip list
$ pip install ライブラリ
$ pip-review --auto
import ライブラリ
from ライブラリ import *
class クラス(親クラス):
    フィールド = 値
    def メソッド(self, 引数):
        処理
オブジェクト = クラス(引数)
オブジェクト.インスタンス変数
オブジェクト.メソッド(引数)
1.0
f'1{x}'
[1]
range(開始, 終了, 間隔)
.append(値)
.remove(位置)
.sort(reverse = True・False)
.count(値)        #個数
.replace(旧, 新)      #置換
.split(区切り)        #分割
.zfill(桁)        #ゼロ埋め
abs(x)            #絶対値
all(x)       #論理積
any(x)       #論理和
len(x)       #長さ
max(x)       #最大値
min(x)       #最小値
sorted(x)   #並べ替え
sum(x)     #合計
... + ...                             # 足す
... - ...                             # 引く
... * ...                             # 掛ける
... ** ...                            # 累乗
... / ...                             # 割る
... % ...                             # 余り
... == ...                            # 等しい
... < ...                             # より小さい
... <= ...                            # 以下
... > ...                             # より大きい
... >= ...                            # 以上
... in ...                            # 含む
... and ...                           # かつ
... or ...                            # または
not ...                               # ではない
with ファイル as 変数:                # ファイルを開く
    ...                               #   処理
if 条件:                              # もし
    ...                               #   処理
elif 条件:                            # でなければもし
    ...                               #   処理
else:                                 # でなければ
    ...                               #   処理
for 変数 in リスト:                   # 繰り返す
    ...                               #   処理
    continue                          #   処理を飛ばす
    break                             #   ループを終わる
while 条件:                           # まで繰り返す
    ...                               #   処理
    continue                          #   処理を飛ばす
    break                             #   ループを終わる
print(出力内容, sep=区切り, end=末尾) # 表示する
input(入力ヒント)                     # 入力する