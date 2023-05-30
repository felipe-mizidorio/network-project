class Rede:
    def __init__(self, nome: str, num_maquinas: int, endereco_rede: str = 'null', endereco_util: str = 'null', endereco_broadcast: str = 'null', mascara: str = 'null'):
        self.nome = nome
        self.num_maquinas = num_maquinas
        self.endereco_rede = endereco_rede
        self.endereco_util = endereco_util
        self.endereco_broadcast = endereco_broadcast
        self.mascara = mascara
        
    def set_endereco_rede(self, endereco_rede: str):
        self.endereco_rede = endereco_rede
        
    def set_endereco_util(self, endereco_util: str):
        self.endereco_util = endereco_util
        
    def set_endereco_broadcast(self, endereco_broadcast: str):
        self.endereco_broadcast = endereco_broadcast
    
    def set_mask(self, mascara: str):
        self.mascara = mascara
    
    def print_rede(self):
        print(f'Nome: {self.nome}')
        print(f'Número de máquinas: {self.num_maquinas}')
        print(f'Endereço Rede: {self.endereco_rede}')
        print(f'Endereço Util: {self.endereco_util}')
        print(f'Endereço Broadcast: {self.endereco_broadcast}')
        print(f'Máscara: {self.mascara}')