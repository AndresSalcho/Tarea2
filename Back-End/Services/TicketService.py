import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import pyodbc
from Factories.Ticket import Ticket

class TicketService:
    def __init__(self) -> None:
        self.con = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};Server=localhost;Database=TAREA_2;Port=1433;UID=sa;PWD=;TrustServerCertificate=yes')

    def selectTicket(self,serie,numero):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_GetTicket {serie},{numero}")
            var = cursor.fetchone()
            return Ticket(var[0],var[1],var[2],var[3],var[4],var[5])
        except:
            return None
        
