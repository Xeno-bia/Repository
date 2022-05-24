'''
with open('txt.txt', mode='w', encoding='utf-8') as var: #ファイルを作成・上書き
    var.write('')

with open('txt.txt', mode='a', encoding='utf-8') as var: #ファイルに追記
    var.write('')
'''

with open('txt.txt', mode='r', encoding='utf-8') as var: #ファイルを取得
    var.read()

from playsound import *
playsound('mp3.mp3') #MP3を再生

list().append(x)       #追加
list().insert(x)       #追加
del x          #削除
list().reverse()      #反転
list().sort()         #並べ替え

set().add(x) #追加
del x               #削除
set() | set() #連結

dict().keys()#キーリスト
dict().values()#値リスト
dict().items() #キー・値リスト
del x #削除
dict() | dict() #連結

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