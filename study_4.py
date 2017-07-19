# study4
# git test

# 4-1
guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
elif guess_me == 7:
    print("just right")

# 4-2
start = 1
guess_me = 7
while True:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it")
    elif start > guess_me:
        print("just right")
        break
    start = start + 1

# 4-3
list = [3, 2, 1, 0]
for number in list:
    print(number)

# 4-4
goo = [gu for gu in range(10) if gu % 2 == 0]
print(goo)

# 4-5
squares = {num: num*num for num in range(10)}
print(squares)

# 4-6
odd = {num for num in range(10) if num % 2 == 1}
print(odd)

# 4-7
for thing in ("Got %s" % num for num in range(10)):
    print(thing)

# 4-8
def good():
    return ['Harry', 'Ron', 'Hermione']
good()

# 4-9 generator
def get_odds():
    for num in range(1, 10, 2):
        yield num


for idx, num in enumerate(get_odds(), 1):
    if idx == 3:
        print("The third odd number is", num)
        break

# 4-10 decorator
def decorater(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@decorater
def greeting():
    print("Greeting, Earthling")

greeting()

# 4-11
class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException:
    print('Cauht an oopps')

# 4-12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A num turns into a monster', 'A hunted yarn shop']
print(dict(zip(titles, plots)))
