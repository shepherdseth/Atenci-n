from cola import Cola


class AtencionCliente:
    def __init__(self):
        self.colas = {  # Se crea un diccionario de colas para cada departamento que toma instancias de clase Cola como definición
            "Servicios Generales": Cola(),
            "Administración": Cola(),
            "Facturación": Cola(),
            "Tecnología": Cola(),
            "Mercadeo": Cola(),
        }
        # Inicializa cliente_atendido, al crear la instancia no habrá clientes por atender.
        self.cliente_atendido = None

    # Los métodos introducen un argumento "departamento" para seleccionar a qué cola de departamento se añadirá.
    def add_customer(self, departamento):
        if departamento in self.colas:
            # Usamos insert.cliente(), método en Cola() para añadir un turno al departamenteo deseado.
            num_cliente = self.colas[departamento].insertar_cliente()
            print(
                f"Cliente {num_cliente} añadido a la cola de {departamento}.")
            print("------------------")
        else:
            print(f"El departamento {departamento} no existe.")

    def attend_customer(self, departamento):
        if departamento in self.colas:
            # El código llamará para atender al primer cliente del departamento que seleccionemos, usando pop.client().
            cliente_atendido = self.colas[departamento].pop_client()
            if cliente_atendido:
                self.cliente_atendido = cliente_atendido
                print(
                    f"Atendiendo al cliente {cliente_atendido} en {departamento}.")
                print("------------------")
            else:
                print(f"No hay clientes esperando en {departamento}.")
                print("------------------")
        else:
            print(f"El departamento {departamento} no existe.")
            print("------------------")

    def current_customer(self):
        return self.cliente_atendido

    def current_state_queue(self):
        # Bucamos en la cola del departamento cuántos elementos hay para mostrar estado actual de las colas de cada departamento.
        for departamento, cola in self.colas.items():
            print(f"Cola del departamento {departamento}:")
            print(f"Tamaño de la cola: {cola.size()}")
            print("------------------")

    def size(self, departamento):
        if departamento in self.colas:  # Devuelve el tamaño de la cola especificada.
            return self.colas[departamento].size()
        else:
            print(f"El departamento {departamento} no existe.")
            print("------------------")
            return None

    def is_empty(self, departamento):
        if departamento in self.colas:  # Verifica si la cosa espeficada está vacía.
            return self.colas[departamento].is_empty()
        else:
            print(f"El departamento {departamento} no existe.")
            print("------------------")
