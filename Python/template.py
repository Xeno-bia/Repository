#----------#
# コメント #
#----------#
# コメント     # 1行
'''コメント''' # 複数行

#------------#
# ライブラリ #
#------------#
# > pip list                        # 一覧
# > pip list --outdate              # 一覧(要更新)
# > pip install ライブラリ          # インストール
# > pip install --update ライブラリ # 更新
# > pip-review --auto               # 更新(一括)
# > pip show ライブラリ             # 情報
from ライブラリ import *            # 呼び出し

#--------#
# クラス #
#--------#
class クラス(親クラス):     # クラス定義
def __init__(self, 引数):   # 変数定義
def メソッド(self, 引数):   # メソッド定義
オブジェクト = クラス(引数) # オブジェクト化
オブジェクト.変数           # 変数呼び出し
オブジェクト.メソッド(引数) # メソッド呼び出し

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


#------#
# 制御 #
#------#
if 条件:              # 分岐
elif 条件:            # 分岐
else:                 # 分岐
for 変数 in コンテナ: # ループ
    continue          # スキップ
    break             # 終了
while 条件:           # ループ
    continue          # スキップ
    break             # 終了

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

#----------#
# datetime #
#----------#
datetime.now()        # 現在日時
datetime.now().year   # 年
datetime.now().month  # 月
datetime.now().day    # 日
datetime.now().hour   # 時
datetime.now().minute # 分
datetime.now().second # 秒

fractions.Fraction(分子, 分母)

sys.version
sys.platform
sys.argv

os.system(コマンド)
os.name()
os.walk(フォルダ)
os.getcwd()
os.mkdir(フォルダ)
os.rename(旧, 新)
os.rmdir(フォルダ)
os.remove(ファイル)

webbrowser.get(ブラウザ).open(url)
webbrowser.get(ブラウザ).open_new_tab(url)

urllib.request.urlopen(url).read()
urllib.request.urlopen(url).close()

numpy.array(リスト)

icrawler.builtin.GoogleImageCrawler(storage = {'root_dir': フォルダ}).crawl(keyword = 検索内容, max_num = 件数)

# > pip install pyinstaller
# > pyinstaller ファイル --onefile (--noconsole)