# 3.8復習課題

# 3-1
years_list = [1993, 1994, 1995, 1996, 1997]
# 3-2
three_years = years_list[3]
# 3-3
max_year = years_list[-1]
# 3-4
things = ["mozzarella", "cinderella", "salmonella"]
# 3-5 リストは代入しなければ中身に変化はない
things[1].capitalize()
# 3-6
bigcheese = things[0].upper()
print(bigcheese)
# 3-7
things.remove("salmonella")
print(things)
# 3-8,9
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise)
# 3-10,11
e2f = {"dog": "chen", "cat": "chat", "walrus": "morse"}
print(e2f)
print(e2f["dog"])
# 3-12,13
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
print(f2e["chen"])
# 3-14
english_word = set(e2f.keys())
print(english_word)
# 3-15,16,17,18
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}},
        'plants': {},
        'others': {}
        }
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
