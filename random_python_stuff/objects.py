anna = {'name': 'Anna',
        'age': 35,
        'cats':True,
        'beard': False,
        'hair_color': 'pink'}

ryan = dict(anna)
ryan['beard'] = True
ryan['hair_color'] = 'Brown'
ryan['name'] = 'Ryan'
ryan['cats'] = 'Nope!'

print(ryan)
print(anna)



class Person(object):
    def __init__(
            self, name, age, cats, beard,
            hair_color=None, works_at_google=True):
        self.name = name
        self.age = age
        self.cats = cats
        self.beard = beard
        self.hair_color = hair_color
        self.googler = works_at_google
        self.hungry = True
        self.kids = []

    def eat(self, food):
        print('OMNOMNOMNOM I AM EATING {food}'.format(food=food))
        self.hungry = False

    def __str__(self):
        anna_string = 'Name: {n}, Age: {a}, Cats:{c}'.format(
            n=self.name, a=self.age, c=self.cats)
        return anna_string

    def give_birth(self, new_person)
        self.kids.append(new_person)

anna = Person(
    name='Anna',
    age=35,
    cats=True,
    beard=False,
    hair_color='pink')
max = Person(
    name='Max',
    age=90,
    cats=False,
    beard=True,
    hair_color='pink')
print(anna.name)
print('Anna is hungry: {h}'.format(h=anna.hungry))
# anna.hungry = False
anna.eat('banana')
print('Anna is hungry: {h}'.format(h=anna.hungry))
print(max.name)
print('Max is hungry: {h}'.format(h=max.hungry))
