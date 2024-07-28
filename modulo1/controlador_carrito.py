
carrito = {}

def controlador_productos(carrito):
    while True:
        try:
            seleccion = int(input("Ingrese qué desea comprar:\n1 - Papa\n2 - Cebolla\n3 - Batata\n4 - Banana\n5 - Manzana\n6 - Zanahoria\n7 - Tomate\n8 - Pimiento\n9 - Ver carrito\n10 - Volver\n"))
            
            if seleccion == 1:
                producto = "Papa"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 2:
                producto = "Cebolla"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 3:
                producto = "Batata"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 4:
                producto = "Banana"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 5:
                producto = "Manzana"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 6:
                producto = "Zanahoria"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 7:
                producto = "Tomate"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 8:
                producto = "Pimiento"
                cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
                carrito[producto] = carrito.get(producto, 0) + cantidad
                print(f"El producto {producto} fue agregado al carrito.")
            elif seleccion == 9:
                print("Carrito actual:", carrito)
                while True:
                    fin_compra = int(input("decea seguir comprando?\n1-si\n2-volver al menu principal\n"))
                    if fin_compra == 1:
                        controlador_productos(carrito)
                    elif fin_compra == 2:
                        return                        
                    else:
                        print("Opción inválida. Inténtelo de nuevo.")   
            elif seleccion == 10:
                return 
            else:
                print("Opción inválida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.")



