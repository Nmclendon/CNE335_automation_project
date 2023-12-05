import os
class Server:
    """ Server class for representing and manipulating servers. """

    # Initializes Server object with its IP.
    def __init__(self, server_ip):
        self.server_ip = server_ip

    # Pings server
    def ping(self):
        echo = os.system('ping -n 1 ' + self.server_ip)
        if echo == 0:
            return
        else:
            return 'Destination cannot be reached.'