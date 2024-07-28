from datetime import datetime, timedelta



class Cliente():
    def __init__(self,nombre,apellido,direccion,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = edad

    def __str__(self):
        if self.edad < 18:
            return f"al ser menor de edad no puede seguir"
        else:
            return f"Buenos días {self.nombre} {self.apellido}, gracias por elegirnos."

    def saludar(self):
        return f"{self.nombre} {self.apellido}, gracias por visitar nuestra pagina."


class Productos(Cliente):
    def __init__(self,nombre, apellido, direccion, edad,carrito_comprado):
        super().__init__(nombre,apellido,direccion,edad)
        self.carrito_comprado = carrito_comprado

    def llevar_carrito(self):
        if not self.carrito_comprado:
            print("El carrito está vacío. No hay productos para llevar.")
        else:
            fecha_compra = datetime.now()
            fecha_entrega = fecha_compra + timedelta(days=5)
            print(f"gracias {self.nombre}, compró {self.carrito_comprado} el día {fecha_compra.strftime('%Y-%m-%d')} y le llegarán a la dirección {self.direccion} el día {fecha_entrega.strftime('%Y-%m-%d')}")
