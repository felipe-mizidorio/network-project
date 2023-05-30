import math
from rede import Rede
    
names_net = ['Matriz_DMZ', 'Matriz_Hosts', 'Filial', 'Servidor']
all_nets = []

for i in range(len(names_net)):
    num_maquinas = int(input(f"Número de máquinas do(a) {names_net[i]}: "))
    all_nets.append(Rede(name = names_net[i], num_machines = num_maquinas))
    
all_nets.sort(key=lambda x: x.num_machines, reverse=True)

for rede in all_nets:
    num_0s = round(math.log2(rede.num_maquinas))
    
    
    
    