import builtins              # 組み込みライブラリ
builtins.print(xxx, sep=sep) #     出力関数
builtins.input(msg)          #     入力関数
builtins.max(ctn)            #     最大値関数
builtins.min(ctn)            #     最小値関数
builtins.sum(ctn)            #     合計関数
builtins.len(ctn)            #     長さ関数
builtins.all(ctn)            #     論理積関数
builtins.any(ctn)            #     論理和関数

int = builtins.int(xxx)      #     整数オブジェクト
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

float = builtins.float(xxx)  #     小数オブジェクト
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

str = builtins.str(xxx)      #     文字列オブジェクト
str.count(xxx)               #         カウントメソッド

builtins.list(xxx)           #     リストオブジェクト
builtins.set(xxx)            #     集合オブジェクト
builtins.dict(xxx)           #     辞書オブジェクト
builtins.range(b, e, s)      #     連番オブジェクト