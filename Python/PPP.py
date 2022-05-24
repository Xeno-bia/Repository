print(                 #出力
    int(123),            #整数
    float(123.0),        #浮動小数点数
    str('123'),          #文字列
    str('123')[start: stop] #取得
    str('123').count('str')        #個数
    str('123').encode('encode')       #エンコード
    str('123').startswith('str')   #先頭判定
    str('123').endswith('str')     #末尾判定
    str('123').isalnum()      #英数字判定
    str('123').isdecimal()    #数字判定
    str('123').isalpha()      #英字判定
    str('123').isupper()      #大文字判定
    str('123').islower()      #小文字判定
    str('123').istitle()      #パスカル判定
    str('123').replace('old', 'new')      #置換
    str('123').split('sep')        #分割
    str('123').upper()        #大文字化
    str('123').lower()        #小文字化
    str('123').title()        #パスカル化
    str('123').index()        #位置
    str('123').zfill(len)        #ゼロ埋め
    list([1, 2, 3]),      #配列
    set([1, 2, 3]),       #集合
    dict(key1 = 1, key2 = 2, key3 = 3),      #辞書
    1 + 2,             #加算, 連結
    1 - 2,             #減算
    1 * 2,             #乗算, 繰り返し
    1 ** 2,            #冪乗
    1 / 2,             #除算
    1 // 2,            #整数除算
    1 % 2,             #剰余
    1 == 2,            #等価
    1 != 2,            #不等価
    1 < 2,             #未満
    1 <= 2,            #以下
    1 > 2,             #超過
    1 >= 2,            #以上
    1 in [1, 2, 3],        #包含
    1 and 2,           #論理積
    1 or 2,            #論理和
    not 1,             #論理否定
    abs(1),            #絶対値
    all([1, 2, 3]),       #論理積
    any([1, 2, 3]),       #論理和
    len([1, 2, 3]),       #長さ
    max([1, 2, 3]),       #最大値
    min([1, 2, 3]),       #最小値
    round(123),          #偶数丸め
    sorted([1, 2, 3]),    #並べ替え
    sum([1, 2, 3]),       #合計
    enumerate([1, 2, 3]), #連番付け
    range(1, 4),    #連番
    input('Please input.'),        #入力
    sep = '\n'
)
