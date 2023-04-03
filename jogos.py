import foca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("******Escolhe o seu jogo!*******")
    print("********************************")

    print("(1) Foca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando foca")
        foca.jogar()
    elif(jogo == 2):
        print("Jogando adinvinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
