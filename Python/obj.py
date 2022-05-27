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
playsound(mp3) #MP3を再生

#ログ
from logging import basicConfig,DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical
basicConfig(filename=file, level=level, format=format)
debug(メッセージ)
info(メッセージ)
warning(メッセージ)
error(メッセージ)
critical(メッセージ)

from janome.tokenizer import Tokenizer
for i in Tokenizer().tokenize(文字列):
    print(i)
    print(i.surface)

a.append(b)          # 追加
a.remove(b)          # 削除
a.sort()             # 昇順
a.sort(reverse=True) # 降順

from builtins import *              # 組み込みライブラリ
builtins.print(xxx, sep=sep) #     出力関数
builtins.input(msg)          #     入力関数
builtins.max(ctn)            #     最大値関数
builtins.min(ctn)            #     最小値関数
builtins.sum(ctn)            #     合計関数

int = builtins.int(num)      #     整数オブジェクト

float = builtins.float(num)  #     小数オブジェクト

str = builtins.str('str')    #     文字列オブジェクト
str.count(str)               #         個数メソッド
str.replace(old, new)        #         置換メソッド
str.split(sep)               #         分割メソッド

builtins.list(xxx)           #     リストオブジェクト

builtins.dict(xxx)           #     辞書オブジェクト

builtins.range(b, e, s)      #     連番オブジェクト