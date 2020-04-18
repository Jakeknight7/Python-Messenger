import socket
import threading
import time
import json

class SERVER:

    def __init__(self):
        self.HOST = ''
        self.PORT = 8080
        self.USERNAMES = {}    # username index with ip address in index
        self.USER_INFO = {}    # ip index with USER class in index
        self.variables = []
        self.new_user_prefix = "new_user:"
        self.message_prefix = "message:"
        self.existing_user_prefix = "existing_user:"

    def NEW_USER(self, user_information, socket, ip):
        # leads with "new_user_prefix"
        information_array = user_information[len(self.new_user_prefix):].split()
        new_user = USER(information_array[0], information_array[1], socket, ip)
        if new_user.USERNAME in self.USERNAMES.keys():
            # username is already taken
            failure = 'Failure'.encode('ascii')
            socket.send(failure)
            return
        self.USER_INFO[socket] = new_user
        self.USERNAMES[new_user.USERNAME] = socket
        success = 'Success'.encode('ascii')
        socket.send(success)
        return

    def EXISTING_USER(self, user_information, socket, ip):
        # leads with "existing_user_prefix"
        information_array = user_information[len(self.existing_user_prefix):].split()
        if information_array[0] in self.USERNAMES.keys():
            if information_array[1] == self.USER_INFO[self.USERNAMES[information_array[0]]].PASSWORD:
                if self.USER_INFO[self.USERNAMES[information_array[0]]].SOCKET == socket:
                    success = 'Success'.encode('ascii')
                    socket.send(success)
                    print("Login attempt for " + information_array[0] + " succesful")
                    return

                # ip doesn't match so remove the entry and add a new one with updated info
                temp = self.USER_INFO[self.USERNAMES[information_array[0]]]
                del self.USER_INFO[self.USERNAMES[information_array[0]]]
                temp.SET_SOCKET(socket)
                self.USER_INFO[socket] = temp
                self.USERNAMES[temp.USERNAME] = socket
                success = 'Success'.encode('ascii')
                socket.send(success)
                print("Login attempt for " + information_array[0] + " succesful")
                return
            else:
                failure = 'Failure'.encode('ascii')
                socket.send(failure)
                print("Login attempt for " + information_array[0] + " failed")
                return
        else:
            failure = 'Failure'.encode('ascii')
            socket.send(failure)
            print("Login attempt for " + information_array[0] + " failed")
            return

    def SEND_MESSAGE(self, user_information, socket, ip):
        print("Sending Message")
        if socket not in self.USER_INFO.keys():
            return False
        information_array = user_information[len(self.message_prefix):].split(':')
        target_users = information_array[0].split(',')
        for user in target_users:
            if user not in self.USERNAMES.keys():
                return False
            # if user == self.USER_INFO[ip].USERNAME or user == '':
            #    pass

        if target_users.sort() not in self.USER_INFO[socket].CHATS:
            self.USER_INFO[socket].CHATS.append(target_users.sort())

        message = user_information[len(information_array[0]) + len(self.message_prefix) + 1:]
        message = self.USER_INFO[socket].USERNAME + ': ' + message
        encoded_message = message.encode('ascii')

        for recipient in target_users:
            recipient_ip = self.USERNAMES[recipient]
            recipient_socket = self.USER_INFO[recipient_ip].SOCKET
            # check to see if the socket is still there
            if recipient_socket is None or recipient == self.USER_INFO[socket].USERNAME:
                continue
            recipient_socket.send(encoded_message)
        socket.send(encoded_message)

    def NEW_INFORMATION(self, connection, ip):
        while True:
            try:
                data = connection.recv(1024)
                if not data:
                    break
                message = data.decode('ascii')
                if message.startswith(self.message_prefix):
                    self.SEND_MESSAGE(message, connection, ip[0])
                elif message.startswith(self.new_user_prefix):
                    self.NEW_USER(message, connection, ip[0])
                elif message.startswith(self.existing_user_prefix):
                    self.EXISTING_USER(message, connection, ip[0])
            except:
                return
        connection.close()


    def RUN_SERVER(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST, self.PORT))
        s.listen(5)

        while True:
            conn, addr = s.accept()
            #with conn:
            print('connected by', addr)
            new_thread = threading.Thread(target=self.NEW_INFORMATION, args=(conn, addr))
            new_thread.start()

class USER:

    def __init__(self, username, password, socket, ip):
        self.USERNAME = username
        self.PASSWORD = password
        self.IP_ADDRESS = ip
        self.SOCKET = socket
        self.CHATS = []

    def SET_IP(self, ip):
        self.IP_ADDRESS = ip

    def SET_SOCKET(self, socket):
        self.SOCKET = socket


MY_SERVER = SERVER()
MY_SERVER.RUN_SERVER()