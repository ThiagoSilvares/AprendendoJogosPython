import Forca
import Adivinhacao

def escolha_jogo():

    print("Escolha o seu jogo!!!")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca!")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhacao!")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()