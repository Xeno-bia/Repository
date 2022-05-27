import datetime as dt
import webbrowser as wb

# 挨拶
now = dt.datetime.now()
hour = now.hour
if 3 <= hour <= 11:
    greet = 'おはようございます。'
elif 12 <= hour <= 17:
    greet = 'こんにちは。'
elif 18 <= hour <= 2:
    greet = 'こんばんは。'
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
if weekday == 0:
    weekday = '月'
elif weekday == 1:
    weekday = '火'
elif weekday == 2:
    weekday = '水'
elif weekday == 3:
    weekday = '木'
elif weekday == 4:
    weekday = '金'
elif weekday == 5:
    weekday = '土'
elif weekday == 6:
    weekday = '日'
today = f'{year}/{month}/{day}({weekday})'
print(
    greet,
    f'今日は {today} です。',
    sep = '\n'
)

while True:
    print(
        'コマンドを選択してください。',
        '検索、終了',
        sep = '\n'
    )
    request = input()

    # ブラウザ
    if request == '検索':
        browser = wb.get()
        browser.open_new_tab('https://www.google.com/?hl=ja')

    # 終了
    elif request == '終了':
        exit()

    # 未定義
    else:
        print('未定義のコマンドです。')