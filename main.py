import math
from rede import Rede
    
names_net = ['Matriz_DMZ', 'Matriz_Hosts', 'Filial', 'Servidor']
all_nets = []

for i in range(len(names_net)):
    num_maquinas = int(input(f"Número de máquinas do(a) {names_net[i]}: "))
    all_nets.append(Rede(nome = names_net[i], num_maquinas = num_maquinas))
    
all_nets.sort(key=lambda x: x.num_maquinas, reverse=True)

for rede in all_nets:
    num_0s = math.ceil(math.log2(rede.num_maquinas))
    num_1s = 32 - num_0s
    mascara_bin = '1' * num_1s + '0' * num_0s
    mascara_dec = [int(mascara_bin[i:i+8], 2) for i in range(0, len(mascara_bin), 8)]
    rede.mascara = '.'.join(map(str, mascara_dec))
    
    
    
    