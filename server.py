def start_server():

    server_config = config['Server']

    # configurations
    HOST = server_config['HOST']
    PORT = int(environ.get('PORT')) #server_config.getint('PORT')
    BUFFER_SIZE = server_config.getint('BUFFER_SIZE')

    # server socket setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(server_config.getint('LIMIT'))

    logging.info('server started %s:%d', HOST, PORT)
