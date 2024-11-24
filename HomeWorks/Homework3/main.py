# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

class basketballer: 
    def __init__(self, fullname, height):
        self.fullname = fullname
        self.height = height

    def toSet(self):
        return {"fullname": self.fullname, "height": self.height}
    
    def __str__(self) -> str:
        return str(self.toSet())

    def __eq__(self, other):
        if isinstance(other, basketballer):
            return self.fullname == other.fullname and self.height == other.height
        return False
    
    def __hash__(self) -> int:
        return hash((self.fullname, self.height))


class basketballers:
    basketballer_list: set
    def __init__(self, basketballer_set = None):
        if basketballer_set is None:
            basketballer_set = set()
        self.basketballer_set = basketballer_set

    def add(self, b):
        if isinstance(b, basketballer):
            self.basketballer_set.add(b)
        else:
            print("can't add this object:", b)
    
    def delete(self, b):
        if isinstance(b, basketballer): 
            if b in self.basketballer_set:
                self.basketballer_set.remove(b)
        else:
            print("had to be an instance of basketballer")

    def change(self, b, newb):
        match = next((x for x in self.basketballer_set if x == b), None)
        match.fullname = newb.fullname
        match.height = newb.height
    
    def __str__(self) -> str:
        return "[" + ",".join([x.__str__() for x in self.basketballer_set]) + "]"
    
bs = basketballers()
bs.add(basketballer("foo", 123))
bs.add(basketballer("foo", 123))
bs.add(basketballer("baz", 1234))
bs.add(basketballer("fuk", 312))
bs.delete(basketballer("fuk", 312))
bs.change(basketballer("foo", 123), basketballer("foo", 321))
print(bs)

# остальные задания не стал делать, они однообразные, время деньги.