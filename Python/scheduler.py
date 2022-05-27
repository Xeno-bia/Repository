import pyperclip

year         = input('年     => ')

month        = input('月     => ')

day          = input('日     => ')

day_of_week  = input('曜日   => ')

begin_hour   = input('開始時 => ').zfill(2)

begin_minute = input('開始分 => ').zfill(2)

end_hour     = input('終了時 => ').zfill(2)

end_minute   = input('終了分 => ').zfill(2)

print(
    'EV3    -  プレスターター(e0), スターター(e1), ベーシック(e2), アドバンス(e3), プロ(e4), マスター(e5)',
    'SPIKE  -  キンダー(s1), ビギナー(s2), チャレンジャー(s3), クリエイター(s4), イノベーター(s5)',
    'その他 -  振替(1), 補講(2), 体験(3), 研修(4)',
    sep = '\n'
)
course = input('コース => ')
if course   == 'e0':
    course = 'プレスターター'
elif course == 'e1':
    course = 'スターター'
elif course == 'e2':
    course = 'ベーシック'
elif course == 'e3':
    course = 'アドバンス'
elif course == 'e4':
    course = 'プロ'
elif course == 'e5':
    course = 'マスター'

elif course == 's1':
    course = 'キンダー'
elif course == 's2':
    course = 'ビギナー'
elif course == 's3':
    course = 'チャレンジャー'
elif course == 's4':
    course = 'クリエイター'
elif course == 's5':
    course = 'イノベーター'

elif course == '1':
    course = '振替'
elif course == '2':
    course = '補講'
elif course == '3':
    course = '体験'
elif course == '4':
    course = '研修'

print(
    '大阪府 -  豊中校(o1), かんらんこども園(o2), 少路校(o3), 山田校(o4)',
    sep = '\n'
)
place = input('場所   => ')
if place   == 'o1':
    place = '豊中校'
elif place == 'o2':
    place = 'かんらんこども園'
elif place == 'o3':
    place = '少路校'
elif place == 'o4':
    place = '山田校'

schedule = f'{year}/{month}/{day}({day_of_week}) {begin_hour}:{begin_minute}-{end_hour}:{end_minute} {course}@{place}'

print(schedule)

pyperclip.copy(schedule)

input()