
class Cola:
    def __init__(self):
        self.clientes = []  # Lista para almacenar los clientes en la cola
        self.num_cliente = 1  # Contador para asignar números de cliente

    def is_empty(self):
        return len(self.clientes) == 0

    def insertar_cliente(self):
        num_cliente = self.num_cliente
        self.clientes.append(num_cliente)  # Añade cliente a la cola
        self.num_cliente += 1  # Incrementa el contador de número de cliente
        return num_cliente

    def pop_client(self):
        if not self.is_empty():
            # Elimina y devuelve el primer cliente de la cola
            return self.clientes.pop(0)
        else:
            return None

    def size(self):
        return len(self.clientes)
