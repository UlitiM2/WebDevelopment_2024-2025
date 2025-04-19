import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 2048


def receive():
    while True:
        try:
            message = client.recv(BUFFER_SIZE).decode('utf-8')
            print(message)
        except:
            print("Ошибка")
            client.close()
            break


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    nickname = input("Введите имя: ")
    client.send(nickname.encode('utf-8'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    while True:
        message = input()
        client.send(message.encode('utf-8'))
