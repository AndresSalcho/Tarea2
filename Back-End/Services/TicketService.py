import pyodbc
from Factories.Ticket import Ticket

class TicketService:
    def __init__(self) -> None:
        self.con = pyodbc.connect('DRIVER={Microsoft ODBC Driver 18 for SQL Server};Server=localhost;Database=TAREA_2;Port=1433;User ID=sa;Password=283235118')

    def selectTicket(self,serie,numero):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_GetTicket {serie},{numero}")
            var = cursor.fetchone()
            return Ticket(var[0],var[1],var[2],var[3],var[4])
        except:
            return None
        