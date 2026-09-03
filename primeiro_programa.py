class camera:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.gravando = False
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"câmera {self.marca} {self.modelo} ligado.")
        else:
            print("a câmera já esta ligada.")
            
    def desligar(self):
        if self.ligado:
            if self.gravando:
                self.parar.gravação()
            self.ligado = False
            print(f"câmera {self.marca} {self.modelo} desligado.")
        else:
            print(f"cãmera {self.marca} {self.modelo} ligado.")
            
                        