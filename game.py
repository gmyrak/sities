import re
import random

PossibleFirst = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

city = {}
region = {}
country = {}

class info:
    def __str__(self):
        #return str(self.__dict__)
        return  '\n\t'.join('{}={}'.format(k, self.__dict__[k])  for k in sorted(self.__dict__.keys()) )


def norma(name):
    name = re.sub(r'\(.+\)', '', name)
    name = re.sub(r'\W', '', name)
    name = re.sub('Ё', 'E', name, flags=re.IGNORECASE)
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


def next_letters(name):
    full_name = get_info(name).name
    full_name = re.sub(r'\(.+\)', '', full_name)
    full_name = full_name.strip()
    lett = set()
    for n in re.split(r'\W', full_name):
        if len(n)==0:
            continue
        i = -1
        while n[i].upper() in 'ЬЪЫ':
            i -= 1
        s = n[i].upper()
        lett.add(s)
        if s == 'Й':
            lett.add('И')
            i -= 1
            while n[i].upper() in 'ЬЪЫ':
                i -= 1
            lett.add(n[i].upper())
        elif s == 'Ё':
            lett.add('Е')
    return lett


class Game():
    def __init__(self):
        self.were_said : set = set()
        self.can_said_by_letter : dict = {}
        for NormName in city.keys():
            k1 = NormName[0]
            words_on_letter : set = self.can_said_by_letter.get(k1, set())
            words_on_letter.add(NormName)
            self.can_said_by_letter[k1] = words_on_letter

    def choose (self, a):
        A: set = self.can_said_by_letter.get(norma(a), {})
        if A:
            AL : list = list(A)
            chouse_word = AL[random.randint(0, len(AL) - 1)]
            A.discard(chouse_word)
            self.were_said.add(chouse_word)
            return chouse_word
        else:
            return None

    def multi_choose(self, A):
        ARR = list(A)
        while ARR:
            pos = random.randint(0, len(ARR)-1)
            ch_letter = ARR.pop(pos)
            ch_word = self.choose(ch_letter)
            if ch_word:
                return ch_word
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
    i = 1
    start = PossibleFirst
    while True:
        w = g.multi_choose(start)
        if w:
            inf = get_info(w)
            nl = next_letters(w)
            print(i, inf.name)
            start = nl
            i += 1
        else:
            break


