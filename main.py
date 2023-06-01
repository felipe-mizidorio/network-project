import math
from rede import Rede

def calcula_endereco(ip: list[int], soma: int) -> list[int]:
    ip[3] += soma
    while ip[3] > 255:
        ip[3] -= 256
        if ip[2] >= 255:
            ip[2] = 0
            ip[1] += 1
        else:
            5000ip[2] += 1    
    return ip
    
names_net = ['Matriz_DMZ', 'Matriz_Hosts', 'Filial', 'Servidor']
all_nets = []

prox_end_livre = [192, 168, 0, 0]

for i in range(len(names_net)):
    num_maquinas = int(input(f"Número de máquinas do(a) {names_net[i]}: "))
    all_nets.append(Rede(nome = names_net[i], num_maquinas = num_maquinas))
    
all_nets.sort(key=lambda x: x.num_maquinas, reverse=True)

for rede in all_nets:
    num_0s = math.ceil(math.log2(rede.num_maquinas + 2))
    num_1s = 32 - num_0s
    mascara_bin = '1' * num_1s + '0' * num_0s
    mascara_dec = [int(mascara_bin[i:i+8], 2) for i in range(0, len(mascara_bin), 8)]
    rede.mascara = '.'.join(map(str, mascara_dec))
    
    num_end_livres = 2 ** num_0s
    
    rede.endereco_rede = '.'.join(map(str, prox_end_livre))
    endereco_inicio = calcula_endereco(prox_end_livre.copy(), 1)
    endereco_fim = calcula_endereco(prox_end_livre.copy(), num_end_livres - 2)
    rede.endereco_util = '.'.join(map(str, endereco_inicio)) + ' - ' + '.'.join(map(str, endereco_fim))
    rede.endereco_broadcast = '.'.join(map(str, calcula_endereco(prox_end_livre.copy(), num_end_livres - 1)))
    
    prox_end_livre = calcula_endereco(prox_end_livre.copy(), num_end_livres)

for rede in all_nets:
    rede.print_rede()
    print()