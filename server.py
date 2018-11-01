from flask import Flask
from flask_cors import CORS
from threading import Thread

client_conn = None
app = Flask(__name__)
CORS(app)

@app.route('/send/<msg>')
def send_mesage_to_client(msg):
    print("Sending: %s" % msg)
    if client_conn != None:
        client_conn.send(msg)
        return "Sent"
    else:
        return "Client not connect"

def socket_srv():
    global client_conn
    HOST = "127.0.0.1"
    PORT = "12345"

    # server socket setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1) # One backlog connection
    while True:
        client_conn, addr = s.accept()
        print("Connected with " + addr[0] + ":" + str(addr[1]))
    return server_socket

def thread_srv(arg):
	socket_srv()
	print("Thread srv end!")

if __name__ == '__main__':
    t = Thread(target = thread_srv, args = (" ", ))
    t.start()
    app.run()

