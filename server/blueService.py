import socket
import threading
from ioHandler import IOHandler

class BluetoothService(IOHandler):
    def __init__(self, server_address, server_port):
        self.service_type = "bluetooth"
        self.server_address = server_address
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.server_socket.bind((server_address, server_port))
        self.clients = []

    def accept_client_connection(self):
        print("Waiting for bluetooth connection...")

        flag = True
        while flag == True:
            client, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}, RFCOMM protocol")
            client_thread = threading.Thread(target=self.handle_client, args=(client, addr))
            client_thread.start()
            self.clients.append(client_thread)
            if threading.activeCount() == 0:
                ans = input("There isn't active connections, stop listening?(y/n)\n")
                if ans == 'y':
                    flag = False


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
                # self.clients.remove(threading.current_thread())
                client_socket.close()
                return False
    
    def start_service(self):
        self.server_socket.listen(10)
        accept_thread = threading.Thread(target=self.accept_client_connection)
        accept_thread.start()


