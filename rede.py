from maquina import Maquina

class Rede:
    def __init__(self, name: str, num_machines: int, ip: str = 'null', mask: str = 'null', machines: list[Maquina] = []):
        self.name = name
        self.num_machines = num_machines
        self.ip = ip
        self.mask = mask
        self.machines = machines
        
    def set_ip(self, ip):
        self.ip = ip
    
    def set_mask(self, mask):
        self.mask = mask
    
    def print_rede(self):
        print(f'Nome: {self.name}')
        print(f'Número de máquinas: {self.num_machines}')
        print(f'IP: {self.ip}')
        print(f'Máscara: {self.mask}')