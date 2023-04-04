print("********************************")
print(" Bem vindo ao game de advinhação")
print("********************************")
32
numero_secreto = 42

chute_str = input("Digite o seu numero: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!!!")
else:
    print("Você errou!!!")

    print("Fim de jogo")