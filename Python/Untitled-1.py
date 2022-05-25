#ライブラリ
$ pip list          # ライブラリ一覧
$ pip install a     # ライブラリインストール
$ pip-review --auto # ライブラリアップデート
import a            # ライブラリ呼び出し

#クラス
class a(b):         # クラス作成
    a = b           # フィールド作成
    def a(self, b): # メソッド作成
        c
a = b(c)            # オブジェクト作成
a.b                 # フィールド呼び出し
a.b(c)              # メソッド呼び出し

a       # 数値
f'a{b}' # 文字列
[a]     # リスト

a.replace(b, c)      # 置換
a.split(b)           # 分割
a.append(b)          # 追加
a.remove(b)          # 削除
a.sort()             # 昇順
a.sort(reverse=True) # 降順
a.count(b)           # 個数

input()         # 入力
print(a, sep=b) # 出力
range(a, b, c)  # 連番
len(a)          # 長さ
sum(a)          # 合計
max(a)          # 最大値
min(a)          # 最小値

a + b   # 足し算
a - b   # 引き算
a * b   # 掛け算
a ** b  # 累乗
a / b   # 割り算
a % b   # 余り
a == b  # イコール
a < b   # 小なり
a <= b  # 小なりイコール
a > b   # 大なり
a >= b  # 大なりイコール
a in b  # 含む
a and b # かつ
a or b  # または
not a   # ではない

with a as b: # ファイル
    c

if a:   # もし-なら
    b
elif a: # でなければもし-なら
    b
else:   # でなければ
    a

for a in b:  # -の分繰り返す
    c
    continue # スキップ
    break    # 終了

while a:     # -の間繰り返す
    b
    continue # スキップ
    break    # 終了

$ pyinstaller a --onefile --noconsole --icon=アイコン # EXE化