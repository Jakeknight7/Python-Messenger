import socket


class Borg(object):

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Connection(Borg):

    def __init__(self):
        Borg.__init__(self)
        if self._shared_state:
            return
        self.HOST = '127.0.0.1'
        self.PORT = 12345
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_connection.connect((self.HOST, self.PORT))
