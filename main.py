import pandas as pd

class Rede:
    def __init__(self, name: str, num_machines: int, ip: str = 'null', mask: str = 'null'):
        self.name = name
        self.num_machines = num_machines
        self.ip = ip
        self.mask = mask
        
    def set_ip(self, ip):
        self.ip = ip
    
    def set_mask(self, mask):
        self.mask = mask
    
    def print_rede(self):
        print(f'Nome: {self.name}')
        print(f'Número de máquinas: {self.num_machines}')
        print(f'IP: {self.ip}')
        print(f'Máscara: {self.mask}')

with open('mascaras.csv') as file:
    all_masks = pd.read_csv(file)
    
names_net = ['Matriz_DMZ', 'Matriz_Hosts', 'Filial', 'Servidor']
all_nets = []
for i in range(len(names_net)):
    all_nets.append(Rede(names_net[i], int(input(f"Número de máquinas do(a) {names_net[i]}: "))))
    
all_nets.sort(key=lambda x: x.num_machines, reverse=True)


    
    