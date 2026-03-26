
def criar_verificador():
    def verificar(valor_minimo, numero):
        if numero >= valor_minimo:
            return "Permitido"
        else:
            return "Bloqueado"
    
