import game

print('Hello!')
try:
    level = float(input('Level='))
except:
    level = 100

print('Level of game = {}%'.format(level))

g = game.Game(level)

print('Я помню {} городов'.format(g.remember_count))

word  = g.multi_choose(game.PossibleFirst)
wait = True



while True:
    inf = game.get_info(word)
    print('{p}{name} // {country}; {region}'.format( **inf.__dict__, p= '>' if wait else '<') )
    next = game.next_letters(word)
    if wait:
        while True:
            word = input('{}>'.format(next))
            if not game.norma(word)[0] in next:
                print('Первая буква должна быть {}'.format(next))
                continue
            acc = g.accept(word)
            if acc==0:
                wait = False
                break
            elif acc==1:
                print('Этот город уже был назван')
            else:
                print('Нет такого города')
    else:
        word = g.multi_choose(next)
        if not word:
            print('Не знаю больше городов')
            break
        else:
            wait = True
