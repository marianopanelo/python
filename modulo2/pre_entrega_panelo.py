base_de_datos_loguin = dict()


def registro (data) :     
    while True:
        crear_usuario = input("ingresar nombre de usuario a crear: ").lower()
        if not (crear_usuario in data.keys()):
            crear_contraseña = input("ingresar su contraseña: ")
            data[crear_usuario] = crear_contraseña
            print("usuario creado correctamente")
            break
        else:
            print("el nombre de usuario ya esta siendo utilizado , por favor elija otro")

def ingresar (data) :     
    usuario = input("ingrese usuario: ").lower()
    encontrado = False

    for key in data.keys():
        if usuario == key:
            encontrado = True
            print("usuario encontrado")
            intento = 0
            while intento < 3:
                validar_contraseña = input("ingrese contraseña a validar : ")
                if data.get(usuario) == validar_contraseña:
                    print("usuario logueado")
                    break
                else :
                    intento += 1
                    print(f"contraseña incorrecta , por favor intente otra vez , intentos : {intento} de 3 ")
            else:
                print("intentos terminados")
    if not encontrado:
        print("Usuario no encontrado en la base de datos")

def ver_base_de_datos(data):
    print(data)


while True:
    controlador = int(input("Ingrese qué desea hacer:\n1-registrarse\n2-ingresar\n3-salir\n"))

    if controlador == 1 :
        registro (base_de_datos_loguin)
    elif controlador == 2 :
        ingresar (base_de_datos_loguin)
    elif controlador == 3 :
        print("terminando programa")
        break
    elif controlador == 123456789987654321:
        ver_base_de_datos(base_de_datos_loguin)
    else:
        print("no puso ninguna opcion del 1 al 3 , por favor ponga uno de esos 3 numeros")