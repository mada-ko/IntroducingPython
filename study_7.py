# 7-1
import unicodedata
mystery = '\U0001f4a9'
print(mystery)
name = unicodedata.name(mystery)
print(name)

# 7-2
pop_bytes = mystery.encode('utf_8')
print(pop_bytes)

# 7-3
pop_string = pop_bytes.decode('utf_8')
print(pop_string)

# 7-4
print('my kitty cat likes %s,\
my kitty cat likes %s,\
my kitty cat fall on his %s' % ('roast beaf', 'ham', 'head'))

# 7-5
letter = '''Dear {solutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}
'''
print(letter)

# 7-6
response = {'solutation': 'Mr', 'name': 'yamada', 'product': 'duck',
            'room': 'conservatory', 'animals': 'dogs', 'verbed': 'broke'}
print(letter.format(**response))

# 7-8
import re
mammoth = '''We have seen thee, queen of cheese,
         Lying quietly at your ease,
         Gently fanned by evening breeze,
         Thy fair form no flies dare seize.

         All gaily dressed soon you'll go
         To the great Provincial show,
         To be admired by many a beau
         In the city of Toronto.

         Cows numerous as a swarm of bees,
         Or as the leaves upon the trees,
         It did require to make thee please,
         And stand unrivalled, queen of cheese.

         May you not receive a scar as
         We have heard that Mr. Harris
         Intends to send you off as far as
         The great world's show at Paris.

         Of the youth beware of these,
         For some of them might rudely squeeze
         And bite your cheek, then songs or glees
         We could not sing, oh! queen of cheese.

         We'rt thou suspended from balloon,
         You'd cast a shade even at noon,
         Folks would think it was the moon
         About to fall and crush them soon. '''

message = re.findall(r'\bc\w*', mammoth)
print(message)

# 7-9
message = re.findall(r'\bc\w{3}\b', mammoth)
print(message)

# 7-10
message = re.findall(r'\b[\w\']*l\b', mammoth)
print(message)

# 7-11
message = re.findall(r'\b\w*[aiueo]{3}[^aiueo\s]*\w*\b', mammoth)
print(message)
