print('Begin')
f = open('base/city.csv', mode='r', encoding='cp1251')


for line in f:
    city_id, country_id, region_id, name = (s.strip('"') for s in line.strip().split(';'))
    print(city_id, country_id, region_id, name)



f.close()
print('Hello')
