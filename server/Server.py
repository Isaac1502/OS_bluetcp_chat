from blueService import BluetoothService

def main():
    server_addr = input("Enter the MAC address of the bluetooth device: ")
    server_port = int(input("Enter the port: "))
    bth = BluetoothService(server_addr, server_port)
    bth.start_server()

if __name__ == '__main__':
    main()