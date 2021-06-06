
from itertools import chain

def get_input_list():
    eventos = []
    in_l = []
    pare = True
    while pare:
        a = input().split()
        #print(a)
        if a == ['0', 'Fuel', 'consumption', '0']: break
        else:
            in_l.append(a)
            if len(in_l) > 0 and in_l[-1][-1] == 'Goal':
                #print(in_l[-1][-1])
                eventos.append(list(chain(*in_l)))
                in_l = []
                if len(eventos) > 50: break # Numero maximo de eventos estabelecidos no enunciado
    return eventos


def eh_possivel_2(vol_tanque, evento):
    consumo = 0
    distancia = 0
    vol_atual = vol_tanque
    dist_perc = []
    combustivel_consumido = []
    vaz = 0
    j = 0
    for i in range(len(evento)):
        if evento[i] == 'consumption': consumo = int(evento[i+1])
        if evento[i] == 'Fuel':
            if int(evento[i-1]) > 0:
                vol_atual -= ((consumo + vaz)/100 * distancia)
                distancia = int(evento[i-1]) - distancia
            else:
                distancia = int(evento[i-1]) - distancia
            #temp.append(distancia)
                #print(f'Volume Consumido(Fuel):{int(((consumo + vaz) * distancia)/100)}')
        #print(f'Aqui consumiu tanque:{vol_atual} L')
            #print(f'Evento:{evento[i]} - Distancia:{distancia} Km - Consumo {consumo} L/100km - Volume Tanque {vol_atual}')
        elif evento[i] == 'station':
            #temp.append(int(evento[i-2]))
            #print(f'tanque antes do posto:{vol_atual} L')
            vol_atual -= ((consumo + vaz)/100 * distancia)
            distancia = int(evento[i-2]) - distancia
            #temp.append(distancia)

            #print(f'Volume Consumido(Posto):{int(((consumo + vaz) * distancia)/100)}')
            vol_atual = vol_tanque # Posto Enche o tanque de novo
            #print(f'tanque apos posto:{vol_atual} L')
            #print(f'Evento:{evento[i]} - Distancia:{distancia} Km - Consumo {consumo} L/100km - Volume Tanque {vol_atual}')
            #print(vol_tanque)
        elif evento[i] == 'Leak':
            #temp.append(int(evento[i-1]))
            vol_atual -= ((consumo + vaz)/100 * distancia)
            vaz += 1

            distancia = int(evento[i-1]) - distancia

            #print(f'Volume Consumido(Vazamento):{int(((consumo + vaz) * distancia)/100)}')
            #print(f'tanque apos vazamento:{vol_atual} L')
            #print(f'Evento:{evento[i]} - Distancia:{distancia} Km - Consumo {consumo} L/100km - Volume Tanque {vol_atual}')
        elif evento[i] == 'Mechanic':
            #temp.append(int(evento[i-1]))

            vol_atual -= ((consumo + vaz)/100 * distancia)
            vaz = 0
            distancia = int(evento[i-1]) - distancia

            #print(f'Volume Consumido(Oficina):{int(((consumo + vaz) * distancia)/100)}')
            #print(f'tanque apos Oficina:{vol_atual} L')
            #print(f'Evento:{evento[i]} - Distancia:{distancia} Km - Consumo {consumo} L/100km - Volume Tanque {vol_atual}')
        elif evento[i] == 'Goal':
            #temp.append(int(evento[i-1]))
            distancia = int(evento[i-1]) - distancia
            vol_atual -= ((consumo + vaz)/100 * distancia)
            #print(f'Evento:{evento[i]} - Distancia:{distancia} Km - Consumo {consumo} L/100km - Volume Tanque {vol_atual}')
            #print(f'Aqui consumiu tanque por ultimo:{vol_atual}')
        #print(f'tanque:{vol_atual}')
    #print(distancia)
    #print(consumo)
    #print(distancia/consumo)
    return vol_atual >= 0

def volume_necessario(evento):
    vazio = 0.000
    cheio = 10000.000
    vol_temp = []
    volume_necessario = 0.000
    # busca binaria discreta
    while vazio < cheio:
        meio = vazio + (cheio - vazio) // 2
        #print(f'meio:{meio}')
        if eh_possivel_2(meio, evento):
           #vol_temp.append(meio)
            cheio = meio
            #print(f'cheio:{cheio}')
        else:
            vazio = meio + 1.010
        #vol_temp.append(vazio)
    #print(vazio)
    volume_necessario = vazio
    return round(volume_necessario, 3)


if __name__ == '__main__':
    t = get_input_list()
    for _ in t:
        #print(_)
        #print(eh_possivel_2(30, _),  sep='----' , end='\n')
        #print(distancia_percorrida(_))
        print('{:.3f}'.format(volume_necessario(_)))
    #volume_necessario
    #for _ in t:
        #print()
        #print(eh_possivel_2(30, _),  sep='----' , end='----')
        #print('{:.3f}'.format(volume_necessario(_)), end='\n')


