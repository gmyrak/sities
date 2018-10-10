import game

print('Hello!')
try:
    level = float(input('Level='))
except:
    level = 100

print('Level of game = {}%'.format(level))

g = game.Game(level)

word  = g.multi_choose(game.PossibleFirst)
wait = True

while True:
    inf = game.get_info(word)
    print('{name} // {country}; {region}'.format( **inf.__dict__ ) )
    next = game.next_letters(word)
    if wait:
        word = input('{}>'.format(next))
        if g.accept(word):
            continue
        else:
            print('Нет такого города')
    break




