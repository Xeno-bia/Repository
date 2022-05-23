# comment

import library

class Class(super):
    def __init__(self, argument):
        pass
    def method(self, argument):
        pass

instance = Class(argument)
instance.variable
instance.method(argument)

True, False
int(number)
float(number)
range(begin, end, step)
str(f'string')
list([value])
dict({key: value})
container[begin: end: step]

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

if condition:
    pass
elif condition:
    pass
else:
    pass

for variable in container:
    pass
    continue
    break

while condition:
    pass
    continue
    break

math.inf
math.pi
math.e
math.sin(number)
math.tan(number)
math.cos(number)
math.factorial(number)
math.gcd(number, number)
math.lcm(number, number)
math.log(number, base)

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

# > pip install pyinstaller
# > pip install pyinstaller
# > pyinstaller file --onefile (--noconsole)