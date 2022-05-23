# cmt

import lib
import math, random, time, calendar, datetime, fractions, sys, os, webbrowser

class Cls(sup):
    def __init__(self, arg):
        pass
    def method(self, arg):
        pass

ins = Cls(arg)
ins.var
ins.meth(arg)

True, False
int(num)
float(num)
range(bgn, end, step)
str(f'str')
list([val])
dict({key: val})
ctn[bgn: end: step]

x + x
x - x
x * x
x ** x
x / x
x // x
x % x
x == x
x < x
x <= x
x > x
x >= x
x in x
x and x
x or x
not x

if cond:
    pass
elif cond:
    pass
else:
    pass

for var in ctn:
    pass
    continue
    break

while cond:
    pass
    continue
    break

math.inf
math.pi
math.e
math.sin(num)
math.tan(num)
math.cos(num)
math.factorial(num)
math.gcd(num, num)
math.lcm(num, num)
math.log(num, num)

random.choice(container)
random.shuffle(container)
random.randint(begin, end)

time.sleep(second)

calendar.calendar(year)
calendar.month(year, month)

datetime.datetime.now()
datetime.datetime.now().year
datetime.datetime.now().month
datetime.datetime.now().day
datetime.datetime.now().hour
datetime.datetime.now().minute
datetime.datetime.now().second

fractions.Fraction(numerator, denominator)

sys.version
sys.platform
sys.argv

os.system(command)
os.name()
os.walk(directory)
os.getcwd()
os.mkdir(directory)
os.rename(old, new)
os.rmdir(directory)
os.remove(file)

webbrowser.get(browser).open(url)
webbrowser.get(browser).open_new_tab(url)

# > py file