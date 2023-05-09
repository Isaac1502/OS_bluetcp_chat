import socket


server_address = "DC:F5:05:5B:39:50"
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((server_address, 4))

print(f"Connected! to {server_address}, RFCOMM protocol")

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        if not data:
            break
        print(f"Received from {server_address}, RFCOMM protocol: {data.decode('utf-8')}")

except OSError:
    pass

print("Disconnected")

client.close()