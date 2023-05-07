import bluetooth
import threading

class BluetoothChatServer:
    def __init__(self, uuid):
        self.uuid = uuid
        self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_socket.bind(("", bluetooth.PORT_ANY))
        self.server_socket.listen(1)
        self.port = self.server_socket.getsockname()[1]
        self.address = self.server_socket.getsockname()[0]
        self.clients = []

    def accept_client_connections(self):
        print("Actividad en el servidor...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Conexión aceptada de {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()
            self.clients.append(client_thread)

    def handle_client(self, client_socket, client_address):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Mensaje recibido de {client_address}: {message}")
                    for c in self.clients:
                        if c != threading.current_thread():
                            c.client_socket.send(f"{client_address}: {message}".encode())
                        
            except :
                print(f"Cliente {client_address} desconectado.")
                self.clients.remove(threading.current_thread())
                client_socket.close()
                return False

    def start_server(self):
        print(f"""
==============================================
   Servidor iniciado
   -------------------------------------------
   BT Address: {self.address}
   BT Port:    {self.port}
----------------------------------------------

""")
        self.server_socket.listen(10)
        accept_thread = threading.Thread(target=self.accept_client_connections)
        accept_thread.start()

#============================
import uuid

uuid = uuid.uuid4()
print(f" UUID: {uuid}")
#uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"
server = BluetoothChatServer(uuid)
server.start_server()

