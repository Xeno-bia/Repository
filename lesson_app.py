from tkinter import *
from tkinter import ttk
from time import *

root = Tk()
root.title("アプリ") #ウィンドウ名
root.state("zoomed") #全画面表示
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

page0 = Frame(root, width=10000, height=5000) #ページ0

frame0 = Frame(page0, width=10000, height=5000) #ページ0用フレーム

class_entry_var = StringVar()
class_label = Label(frame0, text="クラス", font=("Arial", 20, "bold")) #クラス名ラベル
class_entry = Entry(frame0, textvariable=class_entry_var, font=("Arial", 20, "bold")) #クラス名入力欄

level_entry_var = StringVar()
level_label = Label(frame0, text="レベル", font=("Arial", 20, "bold")) #レベルラベル
level_entry = Entry(frame0, textvariable=level_entry_var, font=("Arial", 20, "bold")) #レベル入力欄

no_entry_var = StringVar()
no_label = Label(frame0, text="レッスンNo.", font=("Arial", 20, "bold")) #レッスンNo.ラベル
no_entry = Entry(frame0, textvariable=no_entry_var, font=("Arial", 20, "bold")) #レッスンNo.入力欄

opt_label = Label(frame0, text="オプション", font=("Arial", 20, "bold"))
bom_var = BooleanVar() #月初変数
bom_check = Checkbutton(frame0, text="月初", variable=bom_var, font=("Arial", 20, "bold")) #月初チェックボックス
eom_var = BooleanVar() #月末変数
eom_check = Checkbutton(frame0, text="月末", variable=eom_var, font=("Arial", 20, "bold")) #月末チェックボックス

pair1_label = Label(frame0, text="ペア1", font=("Arial", 20, "bold")) #ペア1ラベル
pair1_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア1-1入力欄
pair1_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア1-2入力欄
pair2_label = Label(frame0, text="ペア2", font=("Arial", 20, "bold")) #ペア2ラベル
pair2_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア2-1入力欄
pair2_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア2-2入力欄
pair3_label = Label(frame0, text="ペア3", font=("Arial", 20, "bold")) #ペア3ラベル
pair3_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア3-1入力欄
pair3_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア3-2入力欄
pair4_label = Label(frame0, text="ペア4", font=("Arial", 20, "bold")) #ペア4ラベル
pair4_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア4-1入力欄
pair4_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア4-2入力欄
pair5_label = Label(frame0, text="ペア5", font=("Arial", 20, "bold")) #ペア5ラベル
pair5_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア5-1入力欄
pair5_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア5-2入力欄
pair6_label = Label(frame0, text="ペア6", font=("Arial", 20, "bold")) #ペア6ラベル
pair6_1_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア6-1入力欄
pair6_2_entry = Entry(frame0, font=("Arial", 20, "bold")) #ペア6-2入力欄

frame0_2 = Frame(page0, width=10000, height=5000)

page1 = Frame(root, width=10000, height=5000) #ページ1

frame1 = Frame(page1, width=10000, height=5000) #ページ1用フレーム

def start_button_func():
    title_label["text"] = f"{class_entry_var.get()}\n({level_entry_var.get()}:{no_entry_var.get()})"
    root.config(menu=menubar)
    page1.tkraise()
start_button = Button(frame0_2, text="開始", command=start_button_func, font=("Arial", 20, "bold")) #開始ボタン

title_label = Label(frame1, text="", font=("Arial", 100, "bold")) #スライドタイトル

menubar = Menu(tearoff = False)
menu = Menu(menubar, tearoff = False)
menubar.add_cascade(label="スライド一覧", menu=menu)
menu.add_command(label="タイトル")





page0.grid(column=0, row=0, sticky=NSEW)

frame0.pack()
frame0_2.pack()

class_label.grid(column=0, row=0, sticky=W, padx=10, pady=15)
class_entry.grid(column=1, row=0, sticky=W, padx=10, pady=15)

level_label.grid(column=0, row=1, sticky=W, padx=10, pady=15)
level_entry.grid(column=1, row=1, sticky=W, padx=10, pady=15)

no_label.grid(column=0, row=2, sticky=W, padx=10, pady=15)
no_entry.grid(column=1, row=2, sticky=W, padx=10, pady=15)

pair1_label.grid(column=0, row=3, sticky=W, padx=10, pady=15)
pair1_1_entry.grid(column=1, row=3, sticky=W, padx=10, pady=15)
pair1_2_entry.grid(column=2, row=3, sticky=W, padx=10, pady=15)
pair2_label.grid(column=0, row=4, sticky=W, padx=10, pady=15)
pair2_1_entry.grid(column=1, row=4, sticky=W, padx=10, pady=15)
pair2_2_entry.grid(column=2, row=4, sticky=W, padx=10, pady=15)
pair3_label.grid(column=0, row=5, sticky=W, padx=10, pady=15)
pair3_1_entry.grid(column=1, row=5, sticky=W, padx=10, pady=15)
pair3_2_entry.grid(column=2, row=5, sticky=W, padx=10, pady=15)
pair4_label.grid(column=0, row=6, sticky=W, padx=10, pady=15)
pair4_1_entry.grid(column=1, row=6, sticky=W, padx=10, pady=15)
pair4_2_entry.grid(column=2, row=6, sticky=W, padx=10, pady=15)
pair5_label.grid(column=0, row=7, sticky=W, padx=10, pady=15)
pair5_1_entry.grid(column=1, row=7, sticky=W, padx=10, pady=15)
pair5_2_entry.grid(column=2, row=7, sticky=W, padx=10, pady=15)
pair6_label.grid(column=0, row=8, sticky=W, padx=10, pady=15)
pair6_1_entry.grid(column=1, row=8, sticky=W, padx=10, pady=15)
pair6_2_entry.grid(column=2, row=8, sticky=W, padx=10, pady=15)

opt_label.grid(column=0, row=9, sticky=W, padx=10, pady=15)
bom_check.grid(column=1, row=9, sticky=NSEW, padx=10, pady=15)
eom_check.grid(column=2, row=9, sticky=NSEW, padx=10, pady=15)

start_button.grid(column=1, row=10, padx=10, pady=15)

page1.grid(column=0, row=0, sticky=NSEW)

frame1.pack()

title_label.grid(column=0, row=0, pady=190)

page0.tkraise()

root.mainloop()