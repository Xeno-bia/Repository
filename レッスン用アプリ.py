#----------#
#モジュール#
#----------#
from tkinter import *

#----#
#設定#
#----#
root = Tk()

#ウィンドウ名
root.title("アプリ")

#全画面表示
root.state("zoomed")

#----#
#入力#
#----#
#ページ
page0 = Frame(root, width=10000, height=5000)

#フレーム
frame0 = Frame(page0, width=10000, height=5000)

#クラス名入力欄
class_entry_var = StringVar()
class_label = Label(frame0, text="クラス", font=("Arial", 20, "bold"))
class_entry = Entry(frame0, textvariable=class_entry_var, font=("Arial", 20, "bold"), width=25)

#レベル入力欄
level_entry_var = StringVar()
level_label = Label(frame0, text="レベル", font=("Arial", 20, "bold"))
level_entry = Entry(frame0, textvariable=level_entry_var, font=("Arial", 20, "bold"), width=25)

#レッスンNo.入力欄
no_entry_var = IntVar()
no_label = Label(frame0, text="レッスンNo.", font=("Arial", 20, "bold"))
no_entry = Entry(frame0, textvariable=no_entry_var, font=("Arial", 20, "bold"), width=25)
no_entry.delete(0, END)

#マンスリーミッション入力欄
mm_entry_var = StringVar()
mm_label = Label(frame0, text="マンスリーミッション", font=("Arial", 20, "bold"))
mm_entry = Entry(frame0, textvariable=mm_entry_var, font=("Arial", 20, "bold"), width=25)

#ミッション入力欄
m_entry_var = StringVar()
m_label = Label(frame0, text="ミッション", font=("Arial", 20, "bold"))
m_entry = Entry(frame0, textvariable=m_entry_var, font=("Arial", 20, "bold"), width=25)

#おうちミッション入力欄
om_entry_var = StringVar()
om_label = Label(frame0, text="おうちミッション", font=("Arial", 20, "bold"))
om_entry = Entry(frame0, textvariable=om_entry_var, font=("Arial", 20, "bold"), width=25)

#オプション入力欄
opt_label = Label(frame0, text="オプション", font=("Arial", 20, "bold"))

#利子
bom_var = BooleanVar()
bom_check = Checkbutton(frame0, text="利子", variable=bom_var, font=("Arial", 20, "bold"))

#開始ボタン
def start_button_func():
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
    menu.add_command(label="じゅぎょうのルール", command=index2)
    def index3():
        page3.tkraise()
    menu.add_command(label="しゅくだいチェック", command=index3)
    def index4():
        page4.tkraise()
    menu.add_command(label="マンスリーミッション", command=index4)
    root.config(menu=menubar)

    #タイトル表示
    title_label["text"] = f"{class_entry_var.get()}\n({level_entry_var.get()}:{no_entry_var.get()})"
    page1.tkraise()

    #クイズNo.設定
    hw_check_1["text"] = f"①クイズ:{no_entry_var.get() - 1} → プラス1ダン"

    #マンスリーミッション設定
    mm["text"] = mm_entry_var.get()

start_button = Button(frame0, text="開始", command=start_button_func, font=("Arial", 20, "bold"))

#--------#
#タイトル#
#--------#
#ページ
page1 = Frame(root, width=10000, height=5000)

#フレーム
frame1 = Frame(page1, width=10000, height=5000)

#タイトル
title_label = Label(frame1, text="", font=("Arial", 100, "bold"))

#------------------#
#じゅぎょうのルール#
#------------------#
#ページ
page2 = Frame(root, width=10000, height=5000)

#フレーム
frame2 = Frame(page2, width=10000, height=5000)

#じゅぎょうのルール
nots = Label(frame2, text="じゅぎょうのルール", font=("Arial", 80, "bold"))
yellow = Label(frame2, text="①はなしをきかない → マイナス1ダン", font=("Arial", 60, "bold"), bg="gold")
red = Label(frame2, text="②ぼうりょく → ダンなし", font=("Arial", 60, "bold"), bg="firebrick1")

#------------------#
#しゅくだいチェック#
#------------------#
#ページ
page3 = Frame(root, width=10000, height=5000)

#フレーム
frame3 = Frame(page3, width=10000, height=5000)

#しゅくだいチェック
hw_check_title = Label(frame3, text="しゅくだいチェック", font=("Arial", 80, "bold"))
hw_check_1 = Label(frame3, text="", font=("Arial", 60, "bold"), bg="spring green")
hw_check_2 = Label(frame3, text="②おうちミッション → プラス1ダン", font=("Arial", 60, "bold"), bg="spring green")

#--------------------#
#マンスリーミッション#
#--------------------#
#ページ
page4 = Frame(root, width=10000, height=5000)

#フレーム
frame4 = Frame(page4, width=10000, height=5000)

#マンスリーミッション
mm_title = Label(frame4, text="マンスリーミッション", font=("Arial", 80, "bold"))
mm = Label(frame4, text="？？？？？？？？？？", font=("Arial", 80, "bold"))

#----------#
#入力(配置)#
#----------#
page0.grid(column=0, row=0, sticky=NSEW)
frame0.grid(column=0, row=0, sticky=NSEW, padx=420, pady=80)
class_label.grid(column=0, row=0, sticky=W, padx=10, pady=15)
class_entry.grid(column=1, columnspan=2, row=0, sticky=W, padx=10, pady=15)
level_label.grid(column=0, row=1, sticky=W, padx=10, pady=15)
level_entry.grid(column=1, columnspan=2, row=1, sticky=W, padx=10, pady=15)
no_label.grid(column=0, row=2, sticky=W, padx=10, pady=15)
no_entry.grid(column=1, columnspan=2, row=2, sticky=W, padx=10, pady=15)
mm_label.grid(column=0, row=3, sticky=W, padx=10, pady=15)
mm_entry.grid(column=1, columnspan=2, row=3, sticky=W, padx=10, pady=15)
m_label.grid(column=0, row=4, sticky=W, padx=10, pady=15)
m_entry.grid(column=1, columnspan=2, row=4, sticky=W, padx=10, pady=15)
om_label.grid(column=0, row=5, sticky=W, padx=10, pady=15)
om_entry.grid(column=1, columnspan=2, row=5, sticky=W, padx=10, pady=15)
opt_label.grid(column=0, row=6, sticky=W, padx=10, pady=15)
bom_check.grid(column=1, row=6, sticky=W, padx=10, pady=15)
start_button.grid(column=0, columnspan=3, row=7, sticky=NSEW, padx=10, pady=15)

#--------------#
#タイトル(配置)#
#--------------#
page1.grid(column=0, row=0, sticky=NSEW)
frame1.pack(pady=180)
title_label.grid(column=0, row=0)

#------------------------#
#じゅぎょうのルール(配置)#
#------------------------#
page2.grid(column=0, row=0, sticky=NSEW)
frame2.grid(column=0, row=0, sticky=NSEW, pady=50)
nots.grid(column=0, row=0, sticky=W, padx=30, pady=40)
yellow.grid(column=0, row=1, sticky=W, padx=30, pady=40)
red.grid(column=0, row=2, sticky=W, padx=30, pady=40)

#------------------------#
#しゅくだいチェック(配置)#
#------------------------#
page3.grid(column=0, row=0, sticky=NSEW)
frame3.grid(column=0, row=0, sticky=NSEW, pady=50)
hw_check_title.grid(column=0, row=0, sticky=W, padx=30, pady=40)
hw_check_1.grid(column=0, row=1, sticky=W, padx=30, pady=40)
hw_check_2.grid(column=0, row=2, sticky=W, padx=30, pady=40)

#--------------------------#
#マンスリーミッション(配置)#
#--------------------------#
page4.grid(column=0, row=0, sticky=NSEW)
frame4.grid(column=0, row=0, sticky=NSEW, pady=50)
mm_title.grid(column=0, row=0, sticky=W, padx=30, pady=40)
mm.grid(column=0, row=1, sticky=W, padx=30, pady=40)

#--------#
#初期画面#
#--------#
page0.tkraise()

#----#
#起動#
#----#
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()