import socket

class GopherServer:
    """
    Serves Gopher directories and files based on controllers that are
    registered with it.
    """
    
    def add(self, controllers):
        """
        Registers controllers with the server.
        """
        pass
        #for controller in controllers:
        #    self.controllers.append(controller)
    
    def run(self):
        """
        Starts the server listening for connections.
        """
        server_socket = socket.socket()
        server_socket.bind(('', 70))
        server_socket.listen(5)
        
        while True:
            connection, address = server_socket.accept()
            
            # Get selector, dispatch to appropriate controller
            requested_selector = connection.recv(1024)
            response = "iWelcome!\tnull\tnull\t1\n."
            
            # Return response from controller
            connection.send(response.encode("utf-8"))
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
