'''
import scipy
import matplotlib
import re
import sklearn
import torch
import PIL
import openpyxl
import cv2
import PySimpleGUI
import janome
import bottle
import flask
import django
import tensorflow
import pygame
import seaborn
import bs4
import chainer
import email
import googletrans
import keras
import logging
import MeCab
import playsound
'''
inf             #無限大
pi              #円周率
e               #ネイピア数
sin(x)       #サイン
tan(x)       #コサイン
cos(x)       #タンジェント
factorial(x)                                                        #階乗
gcd(x, x)                                                           #最大公約数
lcm(x, x)                                                           #最小公倍数
log(x, x)                                                           #対数
mean(x)                                                             #平均
median(x)                                                           #中央値
mode(x)                                                             #最頻値
pvariance(x)                                                        #分散
pstdev(x)                                                           #標準偏差
choice(x)                                                           #選択
shuffle(x)                                                          #シャッフル
randint(x, x)                                                       #乱数
sleep(x)                                                            #待機
calendar(x)                                                         #年間
month(x, x)                                                         #月間
now = now()                                                         #現在日時
now.year                                                            #年
now.month                                                           #月
now.day                                                             #日
now.hour                                                            #時
now.minute                                                          #分
now.second                                                          #秒
datetime(x, x, x, x, x, x)                                          #日時
date(x, x, x)                                                       #日付
time(x, x, x)                                                       #時刻
timedelta(weeks = x, days = x, hours = x, minutes = x, seconds = x) #時差
Fraction(x)                                                      #分数
platform                                                            #OS
version                                                             #Pythonバージョン
argv                                                                #ファイル・コマンドライン引数
system(x)                                                           #コマンド
x = get(x)                                                          #ブラウザ
x.open()                                                           #開く
x.open_new_tab()                                                   #新規タブで開く
array(x)                                                            #numpy配列を作成
x = DataFrame(x)                                             #データフレーム
x[x]                                                             #行呼び出し
x[x]                                                                #列呼び出し
x.loc[x]                                                         #行列呼び出し
x.query(x)                                                          #条件呼び出し
x.sort_values(x)                                               #並べ替え
symbols(x)                                                          #変数
solve(x)                                                            #方程式
expand(x)                                                           #展開
factor(x)                                                           #因数分解
diff(x)                                                             #微分
integrate(x)                                                        #積分
combinations(x) #組み合わせ
permutations(x)#順列

from playsound import *
playsound('mp3') #MP3を再生

'''
#pattern_matching
match object:
    case pattern:
        pass
    case _:
        pass
'''

#ログ
from logging import basicConfig,DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical
basicConfig(filename=file,level=level,format=format)
debug(メッセージ)
info(メッセージ)
warning(メッセージ)
error(メッセージ)
critical(メッセージ)

'''
janome.tokenizer(Tokenizer, .tokenize, .surface)
'''

#例外送出
raise exp('msg')

#例外処理
try:
    ...
except exp:
    ...
else:
    ...
finally:
    ...
#pyinstaller Pythonファイル --onefile --noconsole --icon = アイコン