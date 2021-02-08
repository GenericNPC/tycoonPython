
import socket
hostname = input("Please enter the host you wish to connect to: ")
HOST = hostname  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    stayConnected = 1
    while stayConnected == 1:
        userInput = input("Input: ")
        if (userInput == "quit"):
            stayConnected = 0
        if (userInput != "quit"):
            data = userInput
            data = data.encode()
            s.sendall(data)
            data = s.recv(1024)
            print(data.decode())

print('Received', repr(data))