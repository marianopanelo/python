

def registro(data_registro):
    while True:
        crear_usuario = input("Ingresar nombre de usuario a crear: ").lower()
        if not (crear_usuario in data_registro.keys()):
            crear_contraseña = input("Ingresar su contraseña: ")
            data_registro[crear_usuario] = crear_contraseña
            print("Usuario creado correctamente")
            nombre_usuario = input("Ingrese su nombre: ").lower()
            apellido_usuario = input("Ingrese su apellido: ").lower()
            direccion_usuario = input("Ingrese su dirección: ").lower()
            while True:
                try:
                    edad_usuario = int(input("Por favor ingrese su edad: "))
                    datos_usuario = (nombre_usuario, apellido_usuario, direccion_usuario, edad_usuario)
                    return datos_usuario, crear_usuario
                except ValueError:
                    print("No escribiste un número, para la edad, Por favor, intenta de nuevo.")
            
        else:
            print("el nombre de usuario ya esta siendo utilizado , por favor elija otro")

def ingresar (data_registro) :     
    usuario = input("ingrese usuario: ").lower()
    encontrado = False

    for key in data_registro.keys():
        if usuario == key:
            encontrado = True
            print("usuario encontrado")
            intento = 0
            while intento < 3:
                validar_contraseña = input("ingrese contraseña a validar : ")
                if data_registro.get(usuario) == validar_contraseña:
                    print("usuario logueado")
                    return usuario
                    
                else :
                    intento += 1
                    print(f"contraseña incorrecta , por favor intente otra vez , intentos : {intento} de 3 ")
            else:
                print("intentos terminados")
    if not encontrado:
        print("Usuario no encontrado en la base de datos")

def ver_base_de_datos(data):
    print(data)

