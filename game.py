import re
import random

city = {}
region = {}
country = {}

class info:
    pass


def norma(name):
    name = re.sub(r'\(.+\)', '', name)
    name = re.sub(r'\W', '', name)
    return name.upper()


f = open('base/city.csv', mode='r', encoding='cp1251')
for line in f:
    city_id, country_id, region_id, name = (s.strip('"') for s in line.strip().split(';'))

    c = info()
    c.name = name
    c.city_id = city_id
    c.region_id = region_id
    c.country_id = country_id

    key_name = norma(name)
    city[key_name] = city.get(key_name, ()) + (c,)

f.close()

f = open('base/region.csv', mode='r', encoding='cp1251')
for line in f:
    region_id, country_id, city_id, name = (s.strip('"') for s in line.strip().split(';'))
    region[region_id] = name
f.close()

f = open('base/country.csv', mode='r', encoding='cp1251')
for line in f:
    country_id, city_id, name = (s.strip('"') for s in line.strip().split(';'))
    country[country_id] = name
f.close()


def get_info(name, id=0):
    name = norma(name)
    items = city.get(name)
    if items:
        inf = info()
        inf.count = len(items)
        if id > inf.count-1:
            id = inf.count-1
        inf.order = id
        item = items[id]
        inf.name = item.name
        inf.country = country[item.country_id]
        inf.region = region[item.region_id]
        return inf
    else:
        return None


class Game():
    def __init__(self):
        self.were_said : set = set()
        self.can_said_by_letter : dict = {}
        for NormName in city.keys():
            k1 = NormName[0]
            words_on_letter : set = self.can_said_by_letter.get(k1, set())
            words_on_letter.add(NormName)
            self.can_said_by_letter[k1] = words_on_letter

    def chouse (self, a):
        A: set = self.can_said_by_letter.get(norma(a), {})
        if A:
            AL : list = list(A)
            chouse_word = AL[random.randint(0, len(AL) - 1)]
            A.discard(chouse_word)
            self.were_said.add(chouse_word)
            return chouse_word
        else:
            return None

    def count(self, a):
        return len(self.can_said_by_letter.get(a.upper(), []))

    def accept(self, word):
        word = norma(word)
        if word in self.were_said:
            return False
        A = self.can_said_by_letter.get(word[0])
        if A and word in A:
            A.discard(word)
            self.were_said.add(word)
            return True
        else:
            return False




if __name__ == '__main__':
    g = Game()

    while True:
        w = g.chouse('о')
        if w:
            inf = get_info(w,2)
            print(w, inf.name, inf.region, inf.country, inf.count)
        else:
            break