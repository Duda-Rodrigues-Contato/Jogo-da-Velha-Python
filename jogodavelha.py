'''
1 - Mensagem de boas-vindas
2 - Montar estrutura, mas não printar 
3 - Printar estrutura + mensagem
4 - def para Jogo em si
5 - while (jogador1 == "X")
6 - while (jogador1 == "O")
'''

#4 - def para Jogo em si:
def JogodaVelha():
    #1 - Mensagem de boas-vindas:
    import random
    print("Boas-Vindas ao Jogo da Velha! Escolha quem vai ser o jogador X e qual vai ser o O.")

    #2 - Montar estrutura, mas não printar:
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'

    linha1 = ("{}----{}---{}".format(a,b,c))
    linha2 = ("{}----{}---{}".format(d,e,f))
    linha3 = ("{}----{}---{}".format(g,h,i))

    #3 - Printar estrutura + mensagem:
    print("Essa é a estrutura principal do jogo que será substituido pelos jogadores:")

    print(linha1)
    print(linha2)
    print(linha3)

    jogador1 = "X"
    jogador2 = "O"
    jogadores = "X", "O"
    jogador = random.choice(jogadores)
    print(f"Esse é o jogador que começa:{jogador}!")

    cont = 0
    while(a != b != c or a != d != g or a != e != i or b != e != h or c != f != i):
        if jogador == "X":
            jogador1 = "X"
            jogador2 = "O"
            escolha1 = input("Coloque qual letra você quer que seja substituida:")
            if escolha1 == 'a':
                a = jogador1
                cont +=1
            elif escolha1 == 'b':
                b = jogador1
                cont +=1
            elif escolha1 == 'c':
                c = jogador1
                cont +=1
            elif escolha1 == 'd':
                d = jogador1
                cont +=1
            elif escolha1 == 'e':
                e = jogador1
                cont +=1
            elif escolha1 == 'f':
                f = jogador1
                cont +=1
            elif escolha1 == 'g':
                g = jogador1
                cont +=1
            elif escolha1 == 'h':
                h = jogador1
                cont +=1
            elif escolha1 == 'i':
                i = jogador1
                cont +=1

            linha1 = ("{}----{}---{}".format(a,b,c))
            linha2 = ("{}----{}---{}".format(d,e,f))
            linha3 = ("{}----{}---{}".format(g,h,i))    
            print(linha1)
            print(linha2)
            print(linha3)

            escolha2 = input("Coloque qual letra você quer que seja substituida:")
            if escolha2 == 'a':
                a = jogador2
                cont +=1
            elif escolha2 == 'b':
                b = jogador2
                cont +=1
            elif escolha2 == 'c':
                c = jogador2
                cont +=1
            elif escolha2 == 'd':
                d = jogador2
                cont +=1
            elif escolha2 == 'e':
                e = jogador2
                cont +=1
            elif escolha2 == 'f':
                f = jogador2
                cont +=1
            elif escolha2 == 'g':
                g = jogador2
                cont +=1
            elif escolha2 == 'h':
                h = jogador2
                cont +=1
            elif escolha2 == 'i':
                i = jogador2
                cont +=1

            linha1 = ("{}----{}---{}".format(a,b,c))
            linha2 = ("{}----{}---{}".format(d,e,f))
            linha3 = ("{}----{}---{}".format(g,h,i))    
            print(linha1)
            print(linha2)
            print(linha3)

        elif jogador == "O":
            jogador1 = "O"
            jogador2 = "X"
            escolha1 = input("Coloque qual letra você quer que seja substituida:")
            if escolha1 == 'a':
                a = jogador1
                cont +=1
            elif escolha1 == 'b':
                b = jogador1
                cont +=1
            elif escolha1 == 'c':
                c = jogador1
                cont +=1
            elif escolha1 == 'd':
                d = jogador1
                cont +=1
            elif escolha1 == 'e':
                e = jogador1
                cont +=1
            elif escolha1 == 'f':
                f = jogador1
                cont +=1
            elif escolha1 == 'g':
                g = jogador1
                cont +=1
            elif escolha1 == 'h':
                h = jogador1
                cont +=1
            elif escolha1 == 'i':
                i = jogador1
                cont +=1

            linha1 = ("{}----{}---{}".format(a,b,c))
            linha2 = ("{}----{}---{}".format(d,e,f))
            linha3 = ("{}----{}---{}".format(g,h,i))    
            print(linha1)
            print(linha2)
            print(linha3)

            escolha2 = input("Coloque qual letra você quer que seja substituida:")
            if escolha2 == 'a':
                a = jogador2
                cont +=1
            elif escolha2 == 'b':
                b = jogador2
                cont +=1
            elif escolha2 == 'c':
                c = jogador2
                cont +=1
            elif escolha2 == 'd':
                d = jogador2
                cont +=1
            elif escolha2 == 'e':
                e = jogador2
                cont +=1
            elif escolha2 == 'f':
                f = jogador2
                cont +=1
            elif escolha2 == 'g':
                g = jogador2
                cont +=1
            elif escolha2 == 'h':
                h = jogador2
                cont +=1
            elif escolha2 == 'i':
                i = jogador2
                cont +=1

            linha1 = ("{}----{}---{}".format(a,b,c))
            linha2 = ("{}----{}---{}".format(d,e,f))
            linha3 = ("{}----{}---{}".format(g,h,i))    
            print(linha1)
            print(linha2)
            print(linha3)
    print("Fim de Jogo!")
JogodaVelha()