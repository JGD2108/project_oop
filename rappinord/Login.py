import sqlite3
import stdiomask
from rappinord.Users import Register
from rappinord.user import User
from rappinord.dunord import proceso
from rappinord.domicilios import Domicilios

con = sqlite3.connect("Register.db")
cur = con.cursor()
col = sqlite3.connect("Domiciliario.db")
curr = col.cursor()

class Login():
    def compareUser():
        """ Vamos a tener 2 tablas una de usuarios y otra de administrador, dependiendo de
         lo que el usuario escoja se busca en la tabla"""
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password: ")
        statement = (
            f"SELECT User from Users WHERE User = '{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            col.close()
            Login.getInfo(Usuario)

    def compareAdmin():
        """
        Funcion para iniciar sesion administradores
        """
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password: ")
        statement = (
            f"SELECT User from Admin WHERE User = '{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            col.close()
            proceso.execute()

    def compareDomiciliario():
        """
        Funcion inicio de sesion Domiciliario
        El ususario es se cedula y la contraseña 
        también
        """
        ID = input("Digite su ID: ")
        Password = stdiomask.getpass("Password: ")
        statement = (
            f"SELECT ID from Domiciliarios WHERE ID = '{ID}' AND ID = '{Password}'")
        curr.execute(statement)
        if not curr.fetchone():
            print("Login failed")
        else:
            print("Welcome")
            col.execute(f"UPDATE Domiciliarios SET Estado = 'Available' WHERE Id = '{ID}' ")
            col.commit()
            col.close()
            Domicilios.get_infoD(ID)

    def getInfo(Usuario: str):
        """
        Se obtiene la información del usuario 
        de la bd
        """
        statement = (f"SELECT * FROM Users where User = '{Usuario}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[2]
        cel = record[3]
        id = record[4]
        x = ""
        total = 0
        ubicacion = ""
        user = User(nombre, id, cel, x, total, ubicacion)
        col.close()
        user.Proceso()

    def execute():
        opc1 = int(input("1.Login; 2.Register: "))
        if opc1 == 1:
            while True:
                opc = int(
                    input("1. Usuario; 2. administrador; 3. Domiciliario: "))
                if opc == 1:
                    Login.compareUser()
                    break
                elif opc == 2:
                    Login.compareAdmin()
                    break
                elif opc == 3:
                    Login.compareDomiciliario()
                    break
                else:
                    print("Intente de nuevo con una opción válida")
        else:
            Register.Registrar()
