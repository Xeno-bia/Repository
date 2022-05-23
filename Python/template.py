# コメント

import ライブラリ

class クラス(親クラス):
    def __init__(self, 引数):
        処理
    def メソッド(self, 引数):
        処理

インスタンス = クラス(引数)
インスタンス.変数
インスタンス.メソッド(引数)

True, False
int(数値)
float(数値)
range(開始, 終了, 間隔)
str(f'文字列')
list([値])
dict({キー: 値})
コンテナ[開始: 終了: 間隔]

x + x
x - x
x * x
x ** x
x / x
x // x
x % x
x == x
x < x
x <= x
x > x
x >= x
x in x
x and x
x or x
not x

if 条件:
    処理
elif 条件:
    処理
else:
    処理

for 変数 in コンテナ:
    処理
    continue
    break

while 条件:
    処理
    continue
    break

math.inf
math.pi
math.e
math.sin(数値)
math.tan(数値)
math.cos(数値)
math.factorial(数値)
math.gcd(数値, 数値)
math.lcm(数値, 数値)
math.log(真数, 底数)

random.choice(コンテナ)
random.shuffle(コンテナ)
random.randint(開始, 終了)

time.sleep(秒)

calendar.calendar(年)
calendar.month(年, 月)

datetime.datetime.now()
datetime.datetime.now().year
datetime.datetime.now().month
datetime.datetime.now().day
datetime.datetime.now().hour
datetime.datetime.now().minute
datetime.datetime.now().second

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

# > pip install pyinstaller
# > pyinstaller ファイル --onefile (--noconsole)