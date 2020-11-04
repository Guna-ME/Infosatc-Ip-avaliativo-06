lista = [1,2,3,4,5]

rodar = int(input('''Deseja rodar para direita ou esquerda: 1-Direita 2-Esquerda  ''' ))

if rodar == "1":
    rotacaodireita(lista)

if rodar =="2":
    rotacaoesquerda(lista)

def rotacaodireita(lista):
        lista = lista[-3:] + lista[:-3] 
        print ("Após a rotação para direita:" + str(lista)) 

def rotacaoesquerda(lista):
        lista = lista[3:] + lista[:3] 
        print ("Após a rotação para esquerda:" + str(lista)) 


# Não consigo fazer com que ao selecionar o que deseja vá para as funções;