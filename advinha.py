from random import randint

vitorias = 0
rodadas = 3

print("########  JOGO DA ADIVINHAÇÃO - MELHOR DE 3  ########")

for rodada in range(1, rodadas + 1):
    print(f"\n========== RODADA {rodada} ==========")

    numero_secreto = randint(0, 100)
    chances = 10
    ganhou = False

    while chances > 0:
        chute = input("Chute um número entre 0 e 100: ")

        if chute.isnumeric():
            chute = int(chute)
            chances -= 1

            if chute == numero_secreto:
                print("\n🎉 Parabéns! Você acertou!")
                print(f"O número era {numero_secreto}.")
                print(f"Você ainda tinha {chances} chances.")
                ganhou = True
                vitorias += 1
                break

            elif chute > numero_secreto:
                print("\n❌ Você errou! Dica: é um número menor.")
            else:
                print("\n❌ Você errou! Dica: é um número maior.")

            print(f"Você possui ainda {chances} chances.\n")

        else:
            print("Digite apenas números!")

    if not ganhou:
        print("\n💀 Suas chances acabaram!")
        print(f"O número era {numero_secreto}.")

print("\n########  RESULTADO FINAL  ########")
print(f"Você venceu {vitorias} de {rodadas} rodadas.")

if vitorias == 3:
    print("🏆 Perfeito! Você venceu todas as rodadas!")
elif vitorias == 2:
    print("🥈 Muito bem! Você venceu a maioria das rodadas!")
elif vitorias == 1:
    print("🙂 Você conseguiu vencer uma rodada.")
else:
    print("😢 Você não venceu nenhuma rodada.")

print("########  FIM DE JOGO  ########")
