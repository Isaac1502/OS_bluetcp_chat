from blueService import BluetoothService
from tcpService import TCPService

class Server():
    def __init__(self, service):
        self.service = service
        self.service.start_service()


def main():
    print("=======================   BLUETOOTH SETTINGS   ==================================")
    server_addr = input("Enter the MAC address of the bluetooth device: ")
    server_port = int(input("Enter the port: "))
    bth = BluetoothService(server_addr, server_port)
    print("=================================================================================")
    
    server1 = Server(bth)


if __name__ == '__main__':
    main()