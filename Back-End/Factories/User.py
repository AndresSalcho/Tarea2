class User:
    def __init__(self,ced,nom,ape,em,cont,tel,res) -> None:
        self.cedula = ced
        self.nombres = nom
        self.apellidos = ape
        self.email = em
        self.contrasena = cont
        self.telefono = tel
        self.residencia =res
    
    def ToJSON(self):
        return{
            "cedula": self.cedula,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "email": self.email,
            "contrasena": self.contrasena,
            "telefono": self.telefono,
            "residencia": self.residencia
        }
