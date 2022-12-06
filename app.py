from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("レッスンスライド")
root.attributes("-zoomed", "1")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

bom = False
eom = False
bom = messagebox.askyesno("確認", "月初のレッスンですか?")
if bom == False:
    eom = messagebox.askyesno("確認", "月末のレッスンですか?")

menu =Menu(root)
page = Menu(menu, tearoff=False)

menu.add_cascade(label="ビジュアル", menu=page)

def raise_a():
    a.tkraise()
page.add_command(label="タイトル", command=raise_a)

def raise_b():
    b.tkraise()
page.add_command(label="前回の宿題", command=raise_b)

def raise_c():
    c.tkraise()
if eom == True:
    page.add_command(label="マンスリーミッション", command=raise_c)

def raise_d():
    d.tkraise()
page.add_command(label="ロボット", command=raise_d)

"""
def raise_e():
    e.tkraise()
page.add_command(label="ミッション", command=raise_e)
"""

def raise_f():
    f.tkraise()
page.add_command(label="まとめ", command=raise_f)

def raise_g():
    g.tkraise()
page.add_command(label="今回の宿題", command=raise_g)

def raise_h():
    h.tkraise()
page.add_command(label="ダン", command=raise_h)

root.config(menu=menu)

#タイトル
a = Frame(root, width=10000, height=5000)
a.grid(row=0, column=0, sticky="nsew")

class_name = "ウォーターロボット"
level = "チャレンジャー"
number = "26"
a1 = Label(a, text=f"\n{class_name}", font=("Arial", 120, "bold"))
a1.pack()

ax = Label(a, text="", font=("Arial", 60, "bold"))
ax.pack()

a2 = Label(a, text=f"({level}:レッスン{number})", font=("Arial", 90, "bold"))
a2.pack()

#前回のおうちミッション
b = Frame(root, width=10000, height=5000)
b.grid(row=0, column=0, sticky="nsew")

b1 = Label(b, text="前回の宿題", font=("Arial", 100, "bold"))
b1.place(x=50, y=50)

b2 = Label(b, text="①おうちミッションを出そう!", font=("Arial", 80, "bold"))
b2.place(x=50, y=300)

b3 = Label(b, text="②1ダンもらえるよ!", font=("Arial", 80, "bold"))
b3.place(x=50, y=500)

#マンスリーミッション(月末のみ)
if eom == True:
    c = Frame(root, width=10000, height=5000)
    c.grid(row=0, column=0, sticky="nsew")

    c1 = Label(c, text="マンスリーミッション", font=("Arial", 100, "bold"))
    c1.place(x=50, y=50)

    c2 = Label(c, text="①ああああ", font=("Arial", 80, "bold"))
    c2.place(x=50, y=300)

    c3 = Label(c, text="②ああああ", font=("Arial", 80, "bold"))
    c3.place(x=50, y=500)

#ロボット
d = Frame(root, width=10000, height=5000)
d.grid(row=0, column=0, sticky="nsew")

d1 = Label(d, text="ロボット", font=("Arial", 100, "bold"))
d1.place(x=50, y=50)

d2 = Label(d, text="①パートを決めよう!", font=("Arial", 80, "bold"))
d2.place(x=50, y=300)

d3 = Label(d, text="②ロボットを作ろう!", font=("Arial", 80, "bold"))
d3.place(x=50, y=500)

d3 = Label(d, text="③完成したら改造しよう!", font=("Arial", 80, "bold"))
d3.place(x=50, y=700)

#ミッション

#まとめ
f = Frame(root, width=10000, height=5000)
f.grid(row=0, column=0, sticky="nsew")

f1 = Label(f, text="まとめ", font=("Arial", 100, "bold"))
f1.place(x=50, y=50)

f2 = Label(f, text="ああああ", font=("Arial", 80, "bold"))
f2.place(x=50, y=300)

#今回の宿題
g = Frame(root, width=10000, height=5000)
g.grid(row=0, column=0, sticky="nsew")

g1 = Label(g, text="今回の宿題", font=("Arial", 100, "bold"))
g1.place(x=50, y=50)

g2 = Label(g, text="①クイズ:??", font=("Arial", 80, "bold"))
g2.place(x=50, y=300)

g3 = Label(g, text="②おうちミッション", font=("Arial", 80, "bold"))
g3.place(x=50, y=500)

g4 = Label(g, text="ああああ", font=("Arial", 80, "bold"))
g4.place(x=50, y=700)

#ダン
h = Frame(root, width=10000, height=5000)
h.grid(row=0, column=0, sticky="nsew")

h1 = Label(h, text="ダン", font=("Arial", 100, "bold"))
h1.place(x=50, y=50)

h2 = Label(h, text="①先生からダンをもらおう!", font=("Arial", 80, "bold"))
h2.place(x=50, y=300)

interest = ""
if bom == True:
    interest = " + 利子"
h3 = Label(h, text=f"2 + 1(クイズ) + 1(おうちミッション) + 1(ミッション){interest}", font=("Arial", 40, "bold"))
h3.place(x=50, y=500)

h3 = Label(h, text="②交換する時は先生を呼ぼう!", font=("Arial", 80, "bold"))
h3.place(x=50, y=700)

a.tkraise()

root.mainloop()
