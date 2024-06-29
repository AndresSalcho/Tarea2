import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import pyodbc
from Factories.User import User

class UserService:
    def __init__(self) -> None:
        try:
            self.con = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};Server=localhost;Database=TAREA_2;Port=1433;UID=sa;PWD=;TrustServerCertificate=yes')
        except Exception as e:
            print("Error: " + e)

    def insertUser(self,ced,nom,ape,em,cont,tel,res):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_RegistarUS {ced},\'{nom}\',\'{ape}\',\'{em}\',\'{cont}\',{tel},\'{res}\'")
            self.con.commit()
            return User(ced,nom,ape,em,cont,tel,res)
        except Exception as e:
            print(e)
            return None
    
    def selectUser(self, cedula):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_LoginUS {cedula}")
            var = cursor.fetchone()
            return User(var[0],var[1],var[2],var[3],var[4],var[5],var[6])
        except:
            return None
        
        
    
        
