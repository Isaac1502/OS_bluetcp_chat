import socket
import threading
from abc import ABC, abstractmethod

class IOHandler(ABC):
    @abstractmethod
    def  accept_client_connection(self):
        pass

    @abstractmethod
    def handle_client(self):
        pass

    @abstractmethod
    def start_server(self):
        pass



class BluetoothServer(IOHandler):
    def __init__(self,mac):
        self.mac = mac
        self.server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.server_socket.bind((mac, 4))
        self.clients = []

    def accept_client_connection(self):
        print("Waiting for connection...")

        while True:
            client, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}, RFCOMM protocol")
            client_thread = threading.Thread(target=self.handle_client, args=(client, addr))
            client_thread.start()
            self.clients.append(client_thread)


    def handle_client(self, client_socket, client_address):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if data:
                    print(f"Received from {client_address}: {data}")
                    message = input(f"Enter message to {client_address}, RFCOMM protocol: ")
                    client_socket.send(message.encode('utf-8'))

            except:
                print(f"Client {client_address} disconnected, RFCOMM protocol")
                self.clients.remove(threading.current_thread())
                client_socket.close()
                return False
    
    def start_server(self):
        self.server_socket.listen(10)
        accept_thread = threading.Thread(target=self.accept_client_connection)
        accept_thread.start()



blueServer = BluetoothServer("DC:F5:05:5B:39:50")
blueServer.start_server()

    
