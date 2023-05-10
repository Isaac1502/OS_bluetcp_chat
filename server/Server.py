from blueService import BluetoothService
from tcpService import TCPService

class Server():
    def __init__(self, service):
        self.service = service
        self.service.start_service()

    def print_clients(self):
        print(f"clients via {self.service.service_type}: ")
        for c in self.service.clients:
            print(c)


def main():
    method = int(input("Select the method of communication: \n1. Bluetooth \n2.TCP/IP\n"))
    while method != 1 and method != 2:
        method = int(input("Number not supported. \nSelect the method of communication: \n1. Bluetooth \n2.TCP/IP\n"))
    if method == 1:
        print("=======================   BLUETOOTH SETTINGS   ==================================")
        server_addr = input("Enter the MAC address of the bluetooth device: ")
        server_port = int(input("Enter the port: "))
        bth = BluetoothService(server_addr, server_port)
        print("=================================================================================")
        server = Server(bth)
        server.print_clients()

    elif method == 2:
        print("=======================   TCP/IP SETTINGS   ==================================")
        server_addr = input("Enter the ExtIP address of the device: ")
        server_port = int(input("Enter the port: "))
        tcp= TCPService(server_addr, server_port)
        print("=================================================================================")
        server = Server(tcp)
        server.print_clients()
        
        


if __name__ == '__main__':
    main()