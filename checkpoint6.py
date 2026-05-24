# 1. Método __init__
class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña


usuario1 = Usuario("Maytexu", "FullstacK2026")

print(usuario1.nombre_usuario)
print(usuario1.contraseña)