import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = client_socket.recv(1024).decode().strip()
        if not message:
            break
        print(message)
        if "Game over" in message:
            break
        if "Correct!" in message:
            break
        guess = input("Your guess: ")
        client_socket.sendall(guess.encode())

    client_socket.close()


if __name__ == "__main__":
    main()