# !/usr/bin/env pybricks-micropython
# ? の ?「?」 を使う
from pybricks import ev3brick as brick # pybricks の ev3brick「brick」 を使う
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor) # pybricks.ev3devices の Motor と TouchSensor と ColorSensor と InfraredSensor と UltrasonicSensor と GyroSensor を使う
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align) # pybricks.parameters の Port と Stop と Direction と Button と Color と SoundFile と ImageFile と Align を使う
from pybricks.tools import print, wait, StopWatch # pybricks.tools の print と wait と StopWatch を使う
from pybricks.robotics import DriveBase # pybricks.robotics の DriveBase を使う

# Write your program here
# ?:? の ?「?」 を使う
m_motor = Motor(Port.A) # ポート:A の Mモーター「m_motor」 を使う
left = Motor(Port.B) # ポート:B の Lモーター「left」 を使う
right = Motor(Port.C) # ポート:C の Lモーター「right」 を使う
robot = DriveBase(left, right, 56, 114) # 左タイヤ:left, 右タイヤ:right, タイヤ直径:56mm, タイヤ間距離:114㎜ の 車型ロボット「robot」 を使う
touch_sensor = TouchSensor(Port.S1) # ポート:1 の タッチセンサー「touch_sensor」 を使う
color_sensor = ColorSensor(Port.S3) # ポート:3 の カラーセンサー「color_sensor」 を使う
ultrasonic_sensor = UltrasonicSensor(Port.S4) # ポート:4 の 超音波センサー「ultrasonic_sensor」 を使う

brick.sound.beep() # プログラム開始音を鳴らす

brick.display.text("テキスト", (88, 63)) # ? を x座標:?, y座標:? に表示する
wait(3000) # ?ミリ秒待機する
brick.display.clear() # 画面をリセットする

robot.drive_time(50, 0, 3000) # パワー:?, 向き:? で ?秒ステアリング(小回りはパワー:0)
robot.drive(100, 0) # パワー:?, 向き:? で オン
robot.stop() # オフ

while True: # 無限に繰り返す
    pass
    break # ループ中断

while ...: # ?の間繰り返す
    pass

while not ...: # ?まで繰り返す
    pass

touch_sensor.pressed() # タッチセンサーが押されたかどうか

var = ... # 変数「?」に書き込み(変数名は半角英数とアンダーバー、1文字目に数字は使えない)
var # 変数「?」を読み込み

lst = [..., ..., ...] # 配列「?」に書き込み(配列名は半角英数とアンダーバー、1文字目に数字は使えない)
lst # 配列「?」を読み込み
lst[0] # 配列「?」の?番目を読み込み

for i in lst: # 配列「?」の分繰り返す
    pass

for i in range(3): # ?回繰り返す
    pass

if ...: # もし?なら
    pass
elif ...: #でなければもし?なら
    pass
else: # でなければ
    pass

A == B # 同じ
A != B # 違う
A < B # より小さい
A <= B # 以下
A > B # より大きい
A >= B # 以上

A and B # 全て正しい
A or B # どれかが正しい
not A # ではない
A in B # 含まれる

m_motor.run_time([速度], [時間]) # パワー:?で?秒Mモーターを回転させる(1秒は1000ミリ秒)
m_motor.run_target([速度], [角度]) # パワー:?で?度Mモーターを回転させる

color_sensor.color() # 現在の色
Color.BLACK # 黒色
Color.BLUE # 青色
Color.GREEN # 緑色
Color.YELLOW # 黄色
Color.RED # 赤色
Color.WHITE # 白色
Color.BROWN # 茶色

def santen_set(kyori): # 関数「?(?)」を作る
    pass
    return 0 #戻り値を設定
santen_set(20) # 関数「?(?)」を使う

brick.light(Color.ORANGE) # ライトを?色に光らせる
wait(3000) # ?ミリ秒待機する
Color.GREEN # 緑色
Color.ORANGE # オレンジ色
Color.RED # 赤色

ultrasonic_sensor.distance() # 現在の距離(mm)

color_sensor.reflection() # 現在の反射光

# ライントレース(ON/OFF制御)
while not color_sensor.color() == Color.RED: # 赤色まで繰り返す
    if color_sensor.reflection() > 90:
        robot.drive(100, 45)
    else:
        robot.drive(100, -45)
robot.stop()

brick.buttons() # どのボタンが押されているか(配列)
Button.UP # 上
Button.DOWN # 下
Button.LEFT # 左
Button.RIGHT # 右
Button.CENTER # 中央

# ライントレース(P制御)
target = 50 # 中間値
pg = 1.2 # Pゲイン
while not color_sensor.color() == Color.RED: # 赤色まで繰り返す
    p = (color_sensor.reflection() - target) * pg # (現在の反射光 - 中間値) × Pゲイン
    robot.drive(100, p)
robot.stop()