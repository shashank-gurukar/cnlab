import socket
def client_program():

        host = socket.gethostname()
        port = 19001
        client_socket = socket.socket()
        client_socket.connect((host, port))
        message = input("Enter the String : ")

        while message.lower().strip() != 'exit':

                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print('Received from server: ' + data)
                message = input("Enter the string : ")
        client_socket.close()


if __name__ == '__main__':
        client_program()