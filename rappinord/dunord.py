from rappinord.restaurantes import Cafe, Terrase
from rappinord.domicilios import Domicilios
import sqlite3


class Dunord():
    def __init__(self, terrase: Terrase, domicilios: Domicilios, cafe: Cafe) -> None:
        self.cafe = cafe
        self.terrase = terrase
        self.domicilios = domicilios

    def modificarMenu(self):
        """
        Como sabemos que el menu es un diccionario utilizamos del, update etc..
        """
        # Creación de los objetos
        self.cafe = Cafe(Cafe.menuC)
        self.terrase = Terrase(Terrase.menuT)
        while True:
            print("Que menu desea cambiar?")
            opc = input("1. Cafe; 2. Terrase: ")
            if opc == "1" or opc == "2":
                break
            else:
                print("Escoja una opcion valida: ")
        if opc == "1":
            opc1 = input("1. Eliminar Elemento; 2. Añadir Elemento: ")
            if opc1 == "1":
                print("Recuerde que este es el menu:")
                print(self.cafe.menuC)
                Cambio = input("Digite el elemento a eliminar: ").title()
                data = [Cambio]
                Dunord.Eliminarsql(Dunord, 1, data)
                for key in self.cafe.menuC:
                    if Cambio in key:
                        # Eliminar el cambio solicitado
                        del self.cafe.menuC[key]
                        break
                print("Así queda el Menu")
                print(self.cafe.menuC)  # self.cafe.menuC por que no funciona?
            else:
                Cambio = input("Digite el elemento a añadir: ").title()
                try:
                    precio = input("Digite el precio del elemento: ")
                except ValueError:
                    print("Digite un numero valido: ")
                precio = float(precio)
                new = {Cambio: precio}
                self.cafe.menuC.update(new)
                data = [(Cambio, precio)]
                Dunord.AñadirSql(self, 1, data)
                print("Así queda el menu")
                print(self.cafe.menuC)
        else:
            opc1 = input("1. Eliminar Elmento, 2. Añadir Elemento: ")
            if opc1 == "1":
                print("Recuerde el menu")
                print(self.terrase.menuT)
                Cambio = input("Digite el elemento a eliminar: ").title()
                data = [Cambio]
                Dunord.Eliminarsql(Dunord, 2, data)
                for key in self.terrase.menuT:
                    if Cambio in key:
                        # Eliminar el cambio solicitado
                        del self.terrase.menuT[key]
                        break
                print("Así queda el menu")
                print(self.terrase.menuT)
            else:
                Cambio = input("Digite el elemento a añadir: ").title()
                try:
                    precio = input("Digite el precio del elemento: ")
                except ValueError:
                    print("Digite un numero valido: ")
                precio = float(precio)
                new = {Cambio: precio}
                data = [(Cambio, precio)]
                Dunord.AñadirSql(Dunord, 2, data)
                self.terrase.menuT.update(new)
        return self.cafe.menuC, self.terrase.menuT

    def Eliminarsql(self, opc: int, string: str):
        """
        Esta función ejecuta los comando necesarios para eliminar 
        un dato en específico de una fila de la base de datos
        """
        menu = sqlite3.connect("Menus.db")
        domiciliario = sqlite3.connect("Domiciliario.db")
        d = domiciliario.cursor()
        m = menu.cursor()
        if opc == 1:
            m.execute("DELETE FROM Cafe WHERE Item = ?", (string))
            menu.commit()
        elif opc == 2:
            m.execute("DELETE FROM Terrase WHERE Item=?", (string))
            menu.commit()
        elif opc == 3:
            d.execute("DELETE FROM Domiciliarios WHERE Name = ?", (string))
            domiciliario.commit()
        domiciliario.close()

    def AñadirSql(self, opc: int, data):
        """
        Esta Función ejecuta los comando para añadir
        un nuevo producto a la base de datos
        """
        menus = sqlite3.connect("Menus.db")
        domiciliario = sqlite3.connect("Domiciliario.db")
        m = menus.cursor()
        d = domiciliario.cursor()
        if opc == 1:
            m.executemany(" INSERT INTO Cafe VALUES(?,?)", data)
            menus.commit()
        elif opc == 2:
            m.executemany(" INSERT INTO Terrase VALUES(?,?)", data)
            menus.commit()
        elif opc == 3:
            d.executemany("INSERT INTO Domiciliarios VALUES(?,?,?,?)", data)
            domiciliario.commit()
        domiciliario.close()

    def modificarDomiciliarios(self):
        """
        Registrar un domiciliario o Eliminarlo
        """
        print("ESCOJA QUE DESEA REALIZAR")
        opc = input("1. Registrar; 2.Eliminar: ")
        opcNew = int(opc)
        while opcNew < 1 and opcNew > 2:
            print("Opción invalida")
            opc = input("1. Registrar; 2.Eliminar: ")
            opcNew = int(opc)
        if opcNew == 1:
            Name = input("Digite el nombre: ").title()
            Id = input("Digite el Id: ")
            Cel = input("Digite el Celular: ")
            data = [(Name, Id, Cel, "Ocuppied")]
            Dunord.AñadirSql(Dunord, 3, data)
        else:
            Name = input("Digite el nombre del domiciliario a Eliminar: ")
            data = [Name]
            Dunord.Eliminarsql(Dunord, 3, data)


class proceso():
    def execute():
        while True:
            opc = int(
                input("1. Desea modificar menus; 2. Modificar domiciliarios; 3. Cerrar: "))
            if opc == 1:
                Dunord.modificarMenu(Dunord)
            elif opc == 2:
                Dunord.modificarDomiciliarios(Dunord)
            elif opc == 3:
                break
