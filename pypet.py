print 'Welcome to Pypet!'

cat = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)_',
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

pets = [cat, mouse]


def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1
    print 'omnomom!!'
  else:
    print 'The Pypet is not hungry!'

for pet in pets:
    #print '------------------------------'
    #print 'Hello ' + pet['name'] + '!'
    #print pet['photo']
    #print 'Weight: ' + str(pet['weight'])
    #eed(pet)
    #print 'Weight: ' + str(pet['weight'])
    #print '------------------------------'

print cat
feed(cat)
print(cat)
feed(cat)
