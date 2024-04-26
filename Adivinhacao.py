import random

def jogar():

    print("Bem vindo ao jogo de Adivinhação!!!")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina um nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
        
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute_str = input("Digite o número entre 1 e 100 : ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o número secreto.")
                
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
    print("Fim do jogo!!!")

if(__name__=="__main__"):
    jogar()        