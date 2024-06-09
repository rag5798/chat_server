import socket
import threading
import sys

HEADER = 64
PORT = 5050
SERVER = '10.48.97.70'
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
DIS_MSG = 'Done'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    try:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print('[MESSAGE SENT]')
    except Exception as e:
        print(f"[ERROR SENDING MESSAGE] {e}")

def is_socket_closed(sock):
    try:
        sock.send(b"")
        return False
    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
        return True

def server_response(socket):
    while True:
        try:
            msg_length = socket.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = socket.recv(msg_length).decode(FORMAT)
                # Clear current input line
                sys.stdout.write("\r" + " " * 80 + "\r")
                # Print the server message
                print(f"[SERVER]: {msg}")
                # Redisplay the input prompt
                sys.stdout.write("Please Enter a Message: ")
                sys.stdout.flush()
        except Exception as e:
            print(f"[ERROR RECEIVING MESSAGE] {e}")
            break
    socket.close()
    print("[DISCONNECTED FROM SERVER]")


thread = threading.Thread(target=server_response, args=(client,))
thread.start()

try:
    while not is_socket_closed(client):
        msg = input("Please Enter a Message: ")
        if msg.lower() == "exit":
            send(DIS_MSG)
            break
        send(msg)
except Exception as e:
    print(f"[ERROR] {e}")
finally:
    client.close()
    print("[CONNECTION CLOSED]")