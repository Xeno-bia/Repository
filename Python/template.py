#----------#
# コメント #
#----------#
# コメント                         #1行
'''コメント'''                     #複数行

#------------#
# ライブラリ #
#------------#
# pip list                          #一覧
# pip install ライブラリ            #インストール
# pip-review --auto                 #アップデート
from ライブラリ import *            #インポート

#--------#
# クラス #
#--------#
class クラス(親クラス):             #クラス作成
    def __init__(self, 引数):       #インスタンス変数作成
        self.インスタンス変数 = ...
    def メソッド(self, 引数):       #メソッド作成
        処理
オブジェクト = クラス(引数)         #オブジェクト作成
オブジェクト.インスタンス変数       #インスタンス変数呼び出し
オブジェクト.メソッド(引数)         #メソッド呼び出し

#------#
# 変数 #
#------#
変数 = ...

#------#
# 関数 #
#------#
def 関数(引数): # 関数作成
    処理
関数(引数)      # 関数呼び出し

#----#
# 型 #
#----#
True, False                    # 真偽値
int(数値)                      # 整数
float(数値)                    # 小数
range(開始, 終了, 間隔)        # 連番
str('文字列')                  # 文字列
list([値])                     # 配列
dict({キー: 値})               # 辞書
f'{変数}'                      # 埋め込み
オブジェクト[開始: 終了: 間隔] # 抽出

#--------#
# 演算子 #
#--------#
x + y   # 和
x - y   # 差
x * y   # 積
x ** y  # 冪乗
x / y   # 商
x // y  # 整数商
x % y   # 剰余
x == y  # 等価
x < y   # 未満
x <= y  # 以下
x > y   # 超過
x >= y  # 以上
x in y  # 包含
x and y # 論理積
x or y  # 論理和
not x   # 論理否定


#----#
# 文 #
#----#
with ファイル as 変数: # ファイル処理
    処理

if 条件:               # 分岐
elif 条件:
else:

for 変数 in コンテナ:  # コンテナループ
    処理
    continue           # スキップ
    break              # 終了

while 条件:            # 条件ループ
    処理
    continue           # スキップ
    break              # 終了

#---------#
# builtin #
#---------#

#------#
# math #
#------#
inf             # 無限大
pi              # 円周率
e               # ネイピア数
sin(数値)       # サイン
tan(数値)       # コサイン
cos(数値)       # タンジェント
factorial(数値) # 階乗
gcd(数値, 数値) # 最大公約数
lcm(数値, 数値) # 最小公倍数
log(真数, 底数) # 対数

#--------#
# random #
#--------#
choice(コンテナ)    # 選択
shuffle(コンテナ)   # シャッフル
randint(開始, 終了) # 乱数

#------#
# time #
#------#
sleep(秒) # 待機

#----------#
# calendar #
#----------#
calendar(年)  # 年間
month(年, 月) # 月間

#-------------------#
# datetime.datetime #
#-------------------#
now = now() # 現在日時
now.year    # 年
now.month   # 月
now.day     # 日
now.hour    # 時
now.minute  # 分
now.second  # 秒

#-----------#
# fractions #
#-----------#
Fraction(分子, 分母) # 分数
Fraction(数値)       # 数値 → 分数

#-----#
# sys #
#-----#
platform #OS
version  #Pythonバージョン
argv     #ファイル・コマンドライン引数


#----#
# os #
#----#
system(コマンド) #コマンド

#------------#
# webbrowser #
#------------#
browser = get(ブラウザ)   #ブラウザ
browser.open(URL)         #開く
browser.open_new_tab(URL) #新規タブで開く

#-------#
# numpy #
#-------#
numpy.array(リスト) #numpy配列を作成

# pyinstaller Pythonファイル --onefile --noconsole --icon = アイコン