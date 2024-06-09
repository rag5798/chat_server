import socket
import threading
import queue

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
DIS_MSG = 'Done'

def handle_client(conn, addr, message_queue):
    print(f'[NEW CONNECTION] {addr} connected')
    message_queue.put((conn, addr))
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DIS_MSG:
                    connected = False
                print(f'{addr}: {msg}')
                res = f'{addr}: {msg}'

                res_len = len(res)
                send_len = str(res_len).encode(FORMAT)
                send_len += b' ' * (HEADER - len(send_len))

                if threading.active_count() - 1 > 2:
                    message_queue.put((send_len, res.encode(FORMAT), addr))
        except:
            connected = False

    message_queue.put('done')
    conn.close()
    print(f'[DISCONNECTED] {addr} disconnected')


def start(message_queue):
    server.listen()
    print(f'[LISTENING] IP: {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, message_queue))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')
        if threading.active_count() - 1 == 2:
            connect_thread = threading.Thread(target=connect_two_clients, args=(message_queue,))
            connect_thread.start()


def connect_two_clients(message_queue):
    conn1, addr1 = message_queue.get()
    conn2, addr2 = message_queue.get()
    while True:
        msg_data = message_queue.get()
        if msg_data == 'done':
            break
        else:
            msg_len, msg, addr = msg_data
            try:
                if addr == addr1:
                    conn2.send(msg_len)
                    conn2.send(msg)
                elif addr == addr2:
                    conn1.send(msg_len)
                    conn1.send(msg)
            except (BrokenPipeError, ConnectionResetError):
                break
    conn1.close()
    conn2.close()
    print('[CONNECTION CLOSED] Connection between clients closed')


if __name__ == 'main':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    message_queue = queue.Queue()
    print("[STARTING] Server is Starting")
    start(message_queue)
