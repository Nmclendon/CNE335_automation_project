# Nicholas McLendon
# CNE 335 Fall 2023
# Automate ping/SSH
from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Nicholas McLendon")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    # TODO - Create a Server object
    ec2Server = Server('34.217.207.38')

    # TODO - Call Ping method and print the results
    request = ec2Server.ping()