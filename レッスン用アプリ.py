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
page_0 = Frame(root, width=10000, height=5000)

#フレーム
frame_0 = Frame(page_0, width=10000, height=5000)

#クラス名入力欄
class_entry_var = StringVar()
class_label = Label(frame_0, text="クラス", font=("Arial", 20, "bold"))
class_entry = Entry(frame_0, textvariable=class_entry_var, font=("Arial", 20, "bold"), width=25)

#レベル入力欄
level_entry_var = StringVar()
level_label = Label(frame_0, text="レベル", font=("Arial", 20, "bold"))
level_entry = Entry(frame_0, textvariable=level_entry_var, font=("Arial", 20, "bold"), width=25)

#レッスンNo.入力欄
no_entry_var = IntVar()
no_label = Label(frame_0, text="レッスンNo.", font=("Arial", 20, "bold"))
no_entry = Entry(frame_0, textvariable=no_entry_var, font=("Arial", 20, "bold"), width=25)
no_entry.delete(0, END)

#マンスリーミッション入力欄
mm_entry_var = StringVar()
mm_label = Label(frame_0, text="マンスリーミッション", font=("Arial", 20, "bold"))
mm_entry = Entry(frame_0, textvariable=mm_entry_var, font=("Arial", 20, "bold"), width=25)

#ミッション入力欄
m_entry_var_1 = StringVar()
m_entry_var_2 = StringVar()
m_label = Label(frame_0, text="ミッション", font=("Arial", 20, "bold"))
m_entry_1 = Entry(frame_0, textvariable=m_entry_var_1, font=("Arial", 20, "bold"), width=25)
m_entry_2 = Entry(frame_0, textvariable=m_entry_var_2, font=("Arial", 20, "bold"), width=25)

#おうちミッション入力欄
om_entry_var = StringVar()
om_label = Label(frame_0, text="おうちミッション", font=("Arial", 20, "bold"))
om_entry = Entry(frame_0, textvariable=om_entry_var, font=("Arial", 20, "bold"), width=25)

#オプション入力欄
opt_label = Label(frame_0, text="オプション", font=("Arial", 20, "bold"))

#利子
bom_var = BooleanVar()
bom_check = Checkbutton(frame_0, text="利子", variable=bom_var, font=("Arial", 20, "bold"))

#開始ボタン
def start_button_func():
    #メニューバー
    menubar = Menu(tearoff = False)
    menu = Menu(menubar, tearoff = False)
    menubar.add_cascade(label="スライド一覧", menu=menu)
    def index_0():
        page_0.tkraise()
    menu.add_command(label="入力", command=index_0)
    def index_1():
        page_1.tkraise()
    menu.add_command(label="タイトル", command=index_1)
    def index_2():
        page_2.tkraise()
    menu.add_command(label="じゅぎょうのルール", command=index_2)
    def index_3():
        page_3.tkraise()
    menu.add_command(label="しゅくだいチェック", command=index_3)
    def index_4():
        page_4.tkraise()
    menu.add_command(label="マンスリーミッション", command=index_4)
    def index_5():
        page_5.tkraise()
    menu.add_command(label="くみたて", command=index_5)
    def index_6():
        page_6.tkraise()
    menu.add_command(label="ミッション", command=index_6)
    def index_7():
        page_7.tkraise()
    menu.add_command(label="まとめ", command=index_7)
    root.config(menu=menubar)

    #タイトル表示
    title_label["text"] = f"{class_entry_var.get()}\n({level_entry_var.get()}:{no_entry_var.get()})"
    page_1.tkraise()

    #クイズNo.設定
    hw_check_1["text"] = f"①クイズ:{no_entry_var.get() - 1} → プラス1ダン"

    #マンスリーミッション設定
    mm["text"] = mm_entry_var.get()

    #ミッション設定
    m_1["text"] = f"ロボ:{m_entry_var_1.get()}"
    m_2["text"] = f"ねず:{m_entry_var_2.get()}"

start_button = Button(frame_0, text="開始", command=start_button_func, font=("Arial", 20, "bold"))

#--------#
#タイトル#
#--------#
#ページ
page_1 = Frame(root, width=10000, height=5000)

#フレーム
frame_1 = Frame(page_1, width=10000, height=5000)

#タイトル
title_label = Label(frame_1, text="", font=("Arial", 100, "bold"))

#------------------#
#じゅぎょうのルール#
#------------------#
#ページ
page_2 = Frame(root, width=10000, height=5000)

#フレーム
frame_2 = Frame(page_2, width=10000, height=5000)

#じゅぎょうのルール
nots = Label(frame_2, text="じゅぎょうのルール", font=("Arial", 80, "bold"))
yellow = Label(frame_2, text="①はなしをきかない → マイナス1ダン", font=("Arial", 60, "bold"), bg="gold")
red = Label(frame_2, text="②ぼうりょく → ダンなし", font=("Arial", 60, "bold"), bg="firebrick1")

#------------------#
#しゅくだいチェック#
#------------------#
#ページ
page_3 = Frame(root, width=10000, height=5000)

#フレーム
frame_3 = Frame(page_3, width=10000, height=5000)

#しゅくだいチェック
hw_check_title = Label(frame_3, text="しゅくだいチェック", font=("Arial", 80, "bold"))
hw_check_1 = Label(frame_3, text="", font=("Arial", 60, "bold"), bg="spring green")
hw_check_2 = Label(frame_3, text="②おうちミッション → プラス1ダン", font=("Arial", 60, "bold"), bg="spring green")

#--------------------#
#マンスリーミッション#
#--------------------#
#ページ
page_4 = Frame(root, width=10000, height=5000)

#フレーム
frame_4 = Frame(page_4, width=10000, height=5000)

#マンスリーミッション
mm_title = Label(frame_4, text="マンスリーミッション", font=("Arial", 80, "bold"))
mm = Label(frame_4, text="？？？？？？？？？？", font=("Arial", 50, "bold"))

#--------#
#くみたて#
#--------#
#ページ
page_5 = Frame(root, width=10000, height=5000)

#フレーム
frame_5 = Frame(page_5, width=10000, height=5000)

#くみたて
robot_title = Label(frame_5, text="くみたて", font=("Arial", 80, "bold"))
robot_1 = Label(frame_5, text="①じゃんけんでパートをきめよう！", font=("Arial", 50, "bold"))
robot_2 = Label(frame_5, text="    (かち → ロボにゃん、まけ → ねずボット)", font=("Arial", 50, "bold"))
robot_3 = Label(frame_5, text="②つくるじゅんびをして、まえをむこう！", font=("Arial", 50, "bold"))

#----------#
#ミッション#
#----------#
#ページ
page_6 = Frame(root, width=10000, height=5000)

#フレーム
frame_6 = Frame(page_6, width=10000, height=5000)

#ミッション
m_title = Label(frame_6, text="ミッション", font=("Arial", 80, "bold"))
m_1 = Label(frame_6, text="ロボ:？？？？？？？？？？", font=("Arial", 50, "bold"))
m_2 = Label(frame_6, text="ねず:？？？？？？？？？？", font=("Arial", 50, "bold"))
m_3 = Label(frame_6, text="ミッションクリア → プラス1ダン", font=("Arial", 50, "bold"), bg="spring green")

#------#
#まとめ#
#------#
#ページ
page_7 = Frame(root, width=10000, height=5000)

#フレーム
frame_7 = Frame(page_7, width=10000, height=5000)

#まとめ
summary_title = Label(frame_7, text="まとめ", font=("Arial", 80, "bold"))
summary = Label(frame_7, text="？？？？？？？？？？\n？？？？？？？？？？", font=("Arial", 60, "bold"))

#----#
#配置#
#----#
#入力
page_0.grid(column=0, row=0, sticky=NSEW)
frame_0.grid(column=0, row=0, sticky=NSEW, padx=420, pady=80)
class_label.grid(column=0, row=0, sticky=W, padx=10, pady=15)
class_entry.grid(column=1, columnspan=2, row=0, sticky=W, padx=10, pady=15)
level_label.grid(column=0, row=1, sticky=W, padx=10, pady=15)
level_entry.grid(column=1, columnspan=2, row=1, sticky=W, padx=10, pady=15)
no_label.grid(column=0, row=2, sticky=W, padx=10, pady=15)
no_entry.grid(column=1, columnspan=2, row=2, sticky=W, padx=10, pady=15)
mm_label.grid(column=0, row=3, sticky=W, padx=10, pady=15)
mm_entry.grid(column=1, columnspan=2, row=3, sticky=W, padx=10, pady=15)
m_label.grid(column=0, row=4, sticky=W, padx=10, pady=15)
m_entry_1.grid(column=1, columnspan=2, row=4, sticky=W, padx=10, pady=15)
m_entry_2.grid(column=1, columnspan=2, row=5, sticky=W, padx=10, pady=15)
om_label.grid(column=0, row=6, sticky=W, padx=10, pady=15)
om_entry.grid(column=1, columnspan=2, row=6, sticky=W, padx=10, pady=15)
opt_label.grid(column=0, row=7, sticky=W, padx=10, pady=15)
bom_check.grid(column=1, row=7, sticky=W, padx=10, pady=15)
start_button.grid(column=0, columnspan=3, row=8, sticky=NSEW, padx=10, pady=15)

#タイトル
page_1.grid(column=0, row=0, sticky=NSEW)
frame_1.pack(pady=180)
title_label.grid(column=0, row=0)

#じゅぎょうのルール
page_2.grid(column=0, row=0, sticky=NSEW)
frame_2.grid(column=0, row=0, sticky=NSEW, pady=50)
nots.grid(column=0, row=0, sticky=W, padx=30, pady=40)
yellow.grid(column=0, row=1, sticky=W, padx=30, pady=40)
red.grid(column=0, row=2, sticky=W, padx=30, pady=40)

#しゅくだいチェック
page_3.grid(column=0, row=0, sticky=NSEW)
frame_3.grid(column=0, row=0, sticky=NSEW, pady=50)
hw_check_title.grid(column=0, row=0, sticky=W, padx=30, pady=40)
hw_check_1.grid(column=0, row=1, sticky=W, padx=30, pady=40)
hw_check_2.grid(column=0, row=2, sticky=W, padx=30, pady=40)

#マンスリーミッション
page_4.grid(column=0, row=0, sticky=NSEW)
frame_4.grid(column=0, row=0, sticky=NSEW, pady=50)
mm_title.grid(column=0, row=0, sticky=W, padx=30, pady=40)
mm.grid(column=0, row=1, sticky=W, padx=30, pady=40)

#くみたて
page_5.grid(column=0, row=0, sticky=NSEW)
frame_5.grid(column=0, row=0, sticky=NSEW, pady=40)
robot_title.grid(column=0, row=0, sticky=W, padx=30, pady=30)
robot_1.grid(column=0, row=1, sticky=W, padx=30, pady=40)
robot_2.grid(column=0, row=2, sticky=W, padx=30, pady=40)
robot_3.grid(column=0, row=3, sticky=W, padx=30, pady=40)

#ミッション
page_6.grid(column=0, row=0, sticky=NSEW)
frame_6.grid(column=0, row=0, sticky=NSEW, pady=40)
m_title.grid(column=0, row=0, sticky=W, padx=30, pady=30)
m_1.grid(column=0, row=1, sticky=W, padx=30, pady=40)
m_2.grid(column=0, row=2, sticky=W, padx=30, pady=40)
m_3.grid(column=0, row=3, sticky=W, padx=30, pady=40)

#まとめ
page_7.grid(column=0, row=0, sticky=NSEW)
frame_7.grid(column=0, row=0, sticky=NSEW, pady=50)
summary_title.grid(column=0, row=0, sticky=W, padx=30, pady=40)
summary.grid(column=0, row=1, sticky=W, padx=30, pady=40)

#--------#
#初期画面#
#--------#
page_0.tkraise()

#----#
#起動#
#----#
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()