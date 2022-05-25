# コマンド
'''
$ pip list                                            # ライブラリ一覧
$ pip install lib                                     # ライブラリインストール
$ pip-review --auto                                   # ライブラリアップデート
$ py xxx.py                                           # 実行
$ pyinstaller xxx.py --onefile --noconsole --icon=img # EXE化
'''

# ライブラリ
import lib # ライブラリ呼び出し

# 変数
var = xxx # 変数作成
var       # 変数呼び出し

# 関数
def func(arg): # 関数作成
    xxx
    return rtn # 戻り値
func(arg)      # 関数呼び出し

# クラス
class Cls(sup):          # クラス作成
    fld = xxx            # フィールド作成
    def meth(self, arg): # メソッド作成
        xxx
obj = Cls(arg)           # オブジェクト作成
obj.fld                  # フィールド呼び出し
obj.meth(arg)            # メソッド呼び出し


a.replace(b, c)      # 置換
a.split(b)           # 分割
a.append(b)          # 追加
a.remove(b)          # 削除
a.sort()             # 昇順
a.sort(reverse=True) # 降順

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