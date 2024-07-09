from depart_management import AtencionCliente


def mostrar_menu():
    print("Bienvenido al sistema de atención al cliente")
    print("1. Añadir cliente a la cola")
    print("2. Atender cliente en un departamento")
    print("3. Mostrar cliente en atención")
    print("4. Mostrar estado actual de las colas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    # Main interacciona con la clase AtencionCliente
    sistema_atencion = AtencionCliente()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            departamento = input(
                "Ingrese el departamento: (Servicios Generales, Administración, Facturación, Tecnología o Mercadeo) \n")
            sistema_atencion.add_customer(departamento)

        elif opcion == '2':
            departamento = input("Ingrese el departamento: \n")
            sistema_atencion.attend_customer(departamento)

        elif opcion == '3':
            cliente_atendido = sistema_atencion.current_customer()
            if cliente_atendido:
                print(f"Cliente actualmente en atención: {cliente_atendido}\n")
                print("------------------")
            else:
                print("No hay cliente siendo atendido en este momento.\n")
                print("------------------")

        elif opcion == '4':
            sistema_atencion.current_state_queue()

        elif opcion == '5':
            print("Saliendo del programa...\n")
            print("------------------")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")
            print("------------------")


if __name__ == "__main__":
    main()
