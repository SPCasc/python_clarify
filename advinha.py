from random import randint

print("########  Iniciando o jogo!  ########")


random = randint(0, 100)
chute = 0
chances = 10

# < menor
# > maior
# == igual (comparação)
# != diferente (comparação)
# >= Maior ou Igual (a partir de tal valor)
# <= Menor ou Igual (até tal valor)

while chute != random :
    chute = input("Chute um numero entre 0 e 100")
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random  :
            print('')
            print('Parabens, você venceu¹ O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else :
            print('')
            if chute > random :
                print('Você errou! Dica: é um número menor.')
            else :
                print('Você errou! Dica: É um número maior.')
            print('Você possui ainda {} chances.'.format(chances))
            print('')
        if chances == 0 :
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break
print("########  Iniciando o jogo!  ########")