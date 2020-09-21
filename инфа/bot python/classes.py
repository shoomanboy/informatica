import random
from random import randint
class home():
    """класс по созданию дома"""
    def __init__(self,type,floors,rooms):
        self.type=type
        self.floors=floors
        self.rooms=rooms
    def description_name(self):
        """возвращаем описание дома"""
        return '%s из %s этажей в котором %s комнат(ы)' % (self.type,self.floors,self.rooms)
a=[0]*3
types=['пентахус','коттедж','сруб','кирпичный дом']
b=home('dick',3,5)
print(b.floors)
for i in range(3):
    a[i]=home(random.choice(types),randint(1,10),randint(4,30))
    print(a[i].description_name())
