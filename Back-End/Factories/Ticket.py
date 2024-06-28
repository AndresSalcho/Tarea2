class Ticket:
    def __init__(self,id,date,num,ser,win,pre) -> None:
        self.id_Tiquete = id
        self.fecha = date
        self.numero = num
        self.serie = ser
        self.ganador = win
        self.premio = pre
    def toJSON(self):
        return{
            "id_Tiquete" : self.id_Tiquete,
            "fecha" : self.fecha,
            "numero" : self.numero,
            "serie" : self.serie,
            "ganador" : self.ganador,
            "premio" : self.premio
        }