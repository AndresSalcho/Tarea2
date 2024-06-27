import pyodbc
from Factories.User import User

class UserService:
    def __init__(self) -> None:
        self.con = pyodbc.connect('DRIVER={Microsoft ODBC Driver 18 for SQL Server};Server=localhost;Database=TAREA_2;Port=1433;User ID=sa;Password=283235118')

    def insertUser(self,ced,nom,ape,em,cont,tel,res):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_RegistarUS {ced},{nom},{ape},{em},{cont},{tel}.{res}")
            return User(ced,nom,ape,em,cont,tel,res)
        except:
            return None
    
    def selectUser(self, email):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_LoginUS {email}")
            var = cursor.fetchone()
            return User(var[0],var[1],var[2],var[3],var[4],var[5],var[6])
        except:
            return None
        
        
    
        