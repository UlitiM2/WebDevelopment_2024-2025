import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 2048
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(BUFFER_SIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} вышел из чата!".encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Подключение к {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(BUFFER_SIZE).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Имя пользователя: {nickname}")
        broadcast(f"{nickname} подключился к чату!".encode('utf-8'))
        client.send('Подключение к серверу!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Ожидание подключения...")

    receive()
