# 6-1
class Thing():
    pass

print(Thing)
example = Thing()
print(example)

# 6-2
class Thing2():
    letters = 'abc'

print(Thing2.letters)

# 6-3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

hoge = Thing3()
print(hoge.letters)

# 6-4
class Element():
    def __init__(self, name, simbol, number):
        self.name = name
        self.simbol = simbol
        self.number = number

hoge = Element('Hydrogen', 'H', 1)
print(hoge.name)
print(hoge.number)
print(hoge.simbol)
