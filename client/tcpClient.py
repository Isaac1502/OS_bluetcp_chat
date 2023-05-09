import socket
import threading

class TCPClient():
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def start_client(self):
        print("Starting client...")
        try:
            self.client_socket.connect((self.server_address, self.server_port))
        except OSError:
            pass
        print(f"Connected to {self.server_address}, tcp/ip")
        receive_thread = threading.Thread(target=self.receive_message, args=(self.client_socket, self.server_address))
        receive_thread.start()

    
    def receive_message(self, client_socket, server_address):
        print('Enabled to listen...')
        try:
            while True:
                message = input("Enter message: ")
                client_socket.send(message.encode('utf-8'))
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received from {server_address}, tcp/ip: {data.decode('utf-8')}")

        except OSError:
            pass

        print("Disconnected")
        client_socket.close()

def main():
    server_addr = input("Enter the ExtIP of the device device to connect: ")
    server_port = int(input("Enter the port: "))
    tcpClient = TCPClient(server_addr, server_port)
    tcpClient.start_client()

if __name__ == '__main__':
    main()