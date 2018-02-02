import socket

from .menu import *

class GopherServer:
    """
    Serves Gopher directories and files.
    """
    def run(self):
        """
        Starts the server listening for connections.
        """
        server_socket = socket.socket()
        server_socket.bind(('', 70))
        server_socket.listen(5)
        
        while True:
            connection, address = server_socket.accept()
            
            requested_selector = connection.recv(1024)
            
            response = Menu()
            response.append(MenuItem(
                MenuItemType.MESSAGE,
                "Welcome!"))
            
            connection.send(response.__str__().encode("utf-8"))
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
