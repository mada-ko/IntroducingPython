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
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hoge = Element('Hydrogen', 'H', 1)
print(hoge.name)
print(hoge.number)
print(hoge.symbol)

# 6-5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
Hydrogen.name

# 6-6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
Hydrogen.dump()
print(Hydrogen)

# 6-7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
print(Hydrogen)

# 6-8
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
print(Hydrogen.name)

# 6-10
