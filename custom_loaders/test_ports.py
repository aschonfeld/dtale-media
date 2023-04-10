from dtale.app import is_port_in_use as dtale_port_in_use


def is_port_in_use(port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.bind(('', port))
        return False
    except BaseException as ex:
        print(ex)
        return True
    finally:
        sock.close()


if __name__ == '__main__':

    for port in range(40000,41000):
        if not dtale_port_in_use(port):
            if is_port_in_use(port):
                print(port)
