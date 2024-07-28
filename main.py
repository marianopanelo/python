import sys
from modulo1.controlador_carrito import controlador_productos , carrito
from modulo1.modulo import Cliente , Productos 
from modulo1.controlador_registro import registro , ingresar , ver_base_de_datos

base_de_datos_loguin = dict()
base_de_datos_usuarios = dict()

def bucle_compra (usuario):
    while True:
        controlador_compra = int(input("Ingrese qué desea hacer:\n1-comprar\n2-ver carrito\n3-terminar compra\n4-volver al menu anterior\n"))
        if controlador_compra == 1:
            controlador_productos(carrito)
        elif controlador_compra == 2:
            print("Carrito actual:", carrito)
        elif controlador_compra == 3 :
            cliente = Productos(*usuario, carrito)
            cliente.llevar_carrito()
            print(cliente.saludar())
            sys.exit()
        elif controlador_compra == 4 :
            return
        elif controlador_compra == 123456789987654321:
            ver_base_de_datos(f"base de datos usuario/contraseñas {base_de_datos_loguin}")
            ver_base_de_datos(f"base de datos usuario {base_de_datos_usuarios}")
        else:
            print("no puso ninguna opcion del 1 al 4 , por favor ponga uno de esos 3 numeros")


def primer_controlador ():
    
    while True:
        controlador = int(input("Ingrese qué desea hacer:\n1-registrarce\n2-ingresar\n3-salir\n"))
        

        if controlador == 1 :
            datos_usuario = registro(base_de_datos_loguin)
            print(datos_usuario)
            usuario = Cliente(*datos_usuario[0])
            print(usuario)
            if usuario.edad < 18:
                print(usuario.saludar())
                break
            else:
                base_de_datos_usuarios[datos_usuario[1]] = (datos_usuario[0])
                bucle_compra(datos_usuario[0])

        elif controlador == 2 :
            usuario_a_buscar = ingresar(base_de_datos_loguin)
            if usuario_a_buscar in base_de_datos_usuarios:
                usuario_info = base_de_datos_usuarios[usuario_a_buscar]
                usuario = Cliente(*usuario_info)
                print (usuario) 
                bucle_compra(usuario_info)
            else:
                print("Usuario no encontrado en la base de datos.")
            break  

        elif controlador == 3 :
            print("terminando programa")
            break

        elif controlador == 123456789987654321:
            ver_base_de_datos(f"base de datos usuario/contraseñas {base_de_datos_loguin}")
            ver_base_de_datos(f"base de datos usuario {base_de_datos_usuarios}")


        else:
            print("no puso ninguna opcion del 1 al 3 , por favor ponga uno de esos 3 numeros")




primer_controlador()
