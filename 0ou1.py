from random import randint


num_jogadores = 2

#responsavel por criar a lista de jogadores
jogadores = []#cria uma lista [], range ira criar um loop de numeros aleatorios com random, append ira salvar o numero aleatorio na lista para cade jogador
for i in range(num_jogadores):
    jogadores.append(randint(0, 1))

acertos = 0

for i in range(num_jogadores):
    jogador_i = jogadores [i] #chama o jogador atual na lista de jogadores atravez do indice
    
    for j in range(num_jogadores):#verificar a jogada atual com as outras jogadas
        
        if i != j:#verifica se o jogador atual nao esta sendo comparado com ele memos       
               
                jogador_j = jogadores[j] #chama outro jogador para comprar a jogada
             
                               
                if jogador_i == jogador_j:#verifica se as jogadas sao iguais, se forem incrementa +1 para cada numero igual
                    acertos += 1
                    break

print(f"Numeros escolhidos: {jogadores}")
print(f"Numero de acertos: {acertos}")
