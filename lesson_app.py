#モジュール
from tkinter import *

#設定
root = Tk()
root.title("アプリ") #ウィンドウ名
root.state("zoomed") #全画面表示
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#入力
page0 = Frame(root, width=10000, height=5000) #ページ0

frame0 = Frame(page0, width=10000, height=5000) #ページ0用フレーム

class_entry_var = StringVar()
class_label = Label(frame0, text="クラス", font=("Arial", 20, "bold")) #クラス名ラベル
class_entry = Entry(frame0, textvariable=class_entry_var, font=("Arial", 20, "bold"), width=25) #クラス名入力欄

level_entry_var = StringVar()
level_label = Label(frame0, text="レベル", font=("Arial", 20, "bold")) #レベルラベル
level_entry = Entry(frame0, textvariable=level_entry_var, font=("Arial", 20, "bold"), width=25) #レベル入力欄

no_entry_var = IntVar()
no_label = Label(frame0, text="レッスンNo.", font=("Arial", 20, "bold")) #レッスンNo.ラベル
no_entry = Entry(frame0, textvariable=no_entry_var, font=("Arial", 20, "bold"), width=25) #レッスンNo.入力欄
no_entry.delete(0, END) 

opt_label = Label(frame0, text="オプション", font=("Arial", 20, "bold"))
bom_var = BooleanVar() #利子変数
bom_check = Checkbutton(frame0, text="利子", variable=bom_var, font=("Arial", 20, "bold")) #利子チェックボックス
eom_var = BooleanVar() #マンスリーミッション変数
eom_check = Checkbutton(frame0, text="マンスリーミッション", variable=eom_var, font=("Arial", 20, "bold")) #マンスリーミッションチェックボックス

def start_button_func():
    root.config(menu=menubar)
    title_label["text"] = f"{class_entry_var.get()}\n({level_entry_var.get()}:{no_entry_var.get()})"
    hw_check_1["text"] = f"①クイズ:{no_entry_var.get() - 1} → プラス1ダン"
    page1.tkraise()
start_button = Button(frame0, text="開始", command=start_button_func, font=("Arial", 20, "bold")) #開始ボタン

#メニューバー
menubar = Menu(tearoff = False)
menu = Menu(menubar, tearoff = False)
menubar.add_cascade(label="スライド一覧", menu=menu)
def index0():
    page0.tkraise()
menu.add_command(label="入力", command=index0)
def index1():
    page1.tkraise()
menu.add_command(label="タイトル", command=index1)
def index2():
    page2.tkraise()
menu.add_command(label="わだせんせいのルール", command=index2)
def index3():
    page3.tkraise()
menu.add_command(label="しゅくだいチェック", command=index3)
def index4():
    page4.tkraise()
menu.add_command(label="くみたて", command=index4)

#タイトル
page1 = Frame(root, width=10000, height=5000) #ページ1

frame1 = Frame(page1, width=10000, height=5000) #ページ1用フレーム

title_label = Label(frame1, text="", font=("Arial", 100, "bold")) #スライドタイトル

#わだせんせいのルール
page2 = Frame(root, width=10000, height=5000) #ページ2

frame2 = Frame(page2, width=10000, height=5000) #ページ2用フレーム

nots = Label(frame2, text="わだせんせいのルール", font=("Arial", 80, "bold"))
yellow = Label(frame2, text="①はなしをきかない → マイナス1ダン", font=("Arial", 60, "bold"), bg="gold")
red = Label(frame2, text="②ぼうりょく → ダンなし", font=("Arial", 60, "bold"), bg="firebrick1")

#しゅくだいチェック
page3 = Frame(root, width=10000, height=5000) #ページ3

frame3 = Frame(page3, width=10000, height=5000) #ページ3用フレーム

hw_check_title = Label(frame3, text="しゅくだいチェック", font=("Arial", 80, "bold"))
hw_check_1 = Label(frame3, text="", font=("Arial", 60, "bold"), bg="spring green")
hw_check_2 = Label(frame3, text="②おうちミッション → プラス1ダン", font=("Arial", 60, "bold"), bg="spring green")

#くみたて
page4 = Frame(root, width=10000, height=5000) #ページ4

frame4 = Frame(page4, width=10000, height=5000) #ページ4用フレーム

robot_title = Label(frame4, text="くみたて", font=("Arial", 80, "bold"))
robot_1 = Label(frame4, text="①じゃんけんでパートをきめよう！", font=("Arial", 50, "bold"))
robot_2 = Label(frame4, text="    (かち → ロボにゃん、まけ → ねずボット)", font=("Arial", 50, "bold"))
robot_3 = Label(frame4, text="②つくるじゅんびをして、まえをむこう！", font=("Arial", 50, "bold"))





#入力
page0.grid(column=0, row=0, sticky=NSEW)

frame0.grid(column=0, row=0, sticky=NSEW, padx=445, pady=200)

class_label.grid(column=0, row=0, sticky=W, padx=10, pady=15)
class_entry.grid(column=1, columnspan=2, row=0, sticky=W, padx=10, pady=15)

level_label.grid(column=0, row=1, sticky=W, padx=10, pady=15)
level_entry.grid(column=1, columnspan=2, row=1, sticky=W, padx=10, pady=15)

no_label.grid(column=0, row=2, sticky=W, padx=10, pady=15)
no_entry.grid(column=1, columnspan=2, row=2, sticky=W, padx=10, pady=15)

opt_label.grid(column=0, row=3, sticky=W, padx=10, pady=15)
bom_check.grid(column=1, row=3, sticky=W, padx=10, pady=15)
eom_check.grid(column=2, row=3, sticky=W, padx=10, pady=15)

start_button.grid(column=0, columnspan=3, row=4, sticky=NSEW, padx=10, pady=15)

#タイトル
page1.grid(column=0, row=0, sticky=NSEW)

frame1.pack(pady=180)

title_label.grid(column=0, row=0)

#わだせんせいのルール
page2.grid(column=0, row=0, sticky=NSEW)

frame2.grid(column=0, row=0, sticky=NSEW, pady=100)

nots.grid(column=0, row=0, sticky=W, padx=30, pady=30)
yellow.grid(column=0, row=1, sticky=W, padx=30, pady=30)
red.grid(column=0, row=2, sticky=W, padx=30, pady=30)

#しゅくだいチェック
page3.grid(column=0, row=0, sticky=NSEW)

frame3.grid(column=0, row=0, sticky=NSEW, pady=100)

hw_check_title.grid(column=0, row=0, sticky=W, padx=30, pady=30)
hw_check_1.grid(column=0, row=1, sticky=W, padx=30, pady=30)
hw_check_2.grid(column=0, row=2, sticky=W, padx=30, pady=30)

#くみたて
page4.grid(column=0, row=0, sticky=NSEW)

frame4.grid(column=0, row=0, sticky=NSEW, pady=40)

robot_title.grid(column=0, row=0, sticky=W, padx=30, pady=30)
robot_1.grid(column=0, row=1, sticky=W, padx=30, pady=30)
robot_2.grid(column=0, row=2, sticky=W, padx=30, pady=30)
robot_3.grid(column=0, row=3, sticky=W, padx=30, pady=30)

#初期画面表示
page0.tkraise()

root.mainloop()