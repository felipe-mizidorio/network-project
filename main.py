import pandas as pd
from rede import Rede
from maquina import Maquina

with open('mascaras.csv') as file:
    all_masks = pd.read_csv(file)
    
names_net = ['Matriz_DMZ', 'Matriz_Hosts', 'Filial', 'Servidor']
all_nets = []
for i in range(len(names_net)):
    num_maquinas = int(input(f"Número de máquinas do(a) {names_net[i]}: "))
    all_nets.append(Rede(name = names_net[i], num_machines = num_maquinas, machines=[Maquina(name = f"maquina{i}") for i in range(num_maquinas)]))
    
all_nets.sort(key=lambda x: x.num_machines, reverse=True)

for rede in all_nets:
    for i, qnt in enumerate(all_masks['Quantidade de hosts']):
        if rede.num_machines >= qnt:
            rede.set_mask(all_masks['Máscara'][i])



    
    