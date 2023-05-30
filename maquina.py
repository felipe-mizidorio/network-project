class Maquina:
    def __init__(self, name: str, ip: str = 'null'):
        self.name = name
        self.ip = ip
    
    def set_ip(self, ip):
        self.ip = ip
    
    def print_maquina(self):
        print(f'Nome: {self.name}')
        print(f'IP: {self.ip}')