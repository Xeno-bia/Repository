from calendar import *

c = Calendar()
days = c.itermonthdays2(2022, 6)
for i in days:
    if i[0] == 0:
        continue

    day = str(i[0])
    fday = day.rjust(2, ' ')

    wday = i[1]
    if wday == 0:
        wday = '月'
    elif wday == 1:
        wday = '火'
    elif wday == 2:
        wday = '水'
    elif wday == 3:
        wday = '木'
    elif wday == 4:
        wday = '金'
    elif wday == 5:
        wday = '土'
    elif wday == 6:
        wday = '日'

    schedule = f'{start}({course}){end} >>> '

    x = f'{day}({wday}) | {schedule}'
    print(x)


'''
EV3
    幼 - 幼稚園
    St - スターター
    Ba - ベーシック
    Ad - アドバンス
    Pr - プロ
    Ma - マスター

SPIKE
    幼 - 幼稚園
    Ki - キンダー
    Be - ビギナー
    Ch - チャレンジャー
    Cr - クリエイター
    In - イノベーター

 1(水) | 00:00(Ch)03:00 >>> 04:00(幼)07:00
 2(木) | 
 3(金) | 
 4(土) | 
 5(日) | 
 6(月) | 
 7(火) | 
 8(水) | 
 9(木) | 
10(金) | 
11(土) | 
12(日) | 
13(月) | 
14(火) | 
15(水) | 
16(木) | 
17(金) | 
18(土) | 
19(日) | 
20(月) | 
21(火) | 
22(水) | 
23(木) | 
24(金) | 
25(土) | 
26(日) | 
27(月) | 
28(火) | 
29(水) | 
30(木) | 
'''