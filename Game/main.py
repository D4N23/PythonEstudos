import random
print("********************************")
print(" Bem vindo ao game de advinhação")
print("********************************")

numero_secreto = round(random.randrange(1, 100))
total_de_tentativa = 0

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")
nivel = int(input("Defina o nivel:"))
if(nivel == 1):
    total_de_tentativa = 15
elif (nivel == 2)
    total_de_tentativa = 10
elif (nivel == 3)
    total_de_tentativa = 5

for rodada in range(1,total_de_tentativa + 1):

    print("Tentativa {} do total de {}".format(rodada, total_de_tentativa))
    chute_str = input("Digite um numero(De 1 a 100 seu animal!!!): ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100! seu burro!!!")
        continue

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if(acertou):
        print("Você acertou!!!")
        break
    else:
        if(menor):
            print("Você errou, o valor chutado é menor!")
        elif(maior):
            print("Você errou, o valor chutado é maior!")
print("Fim de Papo o numero correto era o {}".format(numero_secreto))