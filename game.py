import re

city = {}
region = {}
country = {}

class city_info:
    pass


def norma(name):
    name = re.sub(r'\(.+\)', '', name)
    name = re.sub(r'\W', '', name)
    return name.upper()


f = open('base/city.csv', mode='r', encoding='cp1251')
for line in f:
    city_id, country_id, region_id, name = (s.strip('"') for s in line.strip().split(';'))

    c = city_info()
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


if __name__ == '__main__':

    for city_name in sorted(city.keys()):
        for c in city[city_name]:
            print('{} | {}; {}; {}'.format(city_name, c.name, region[c.region_id], country[c.country_id]))
            #print('{} '.format(c.name))

