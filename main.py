# Nicholas McLendon
# CNE 335 Fall 2023
# This script pings and then connects to an Ubuntu EC2 to install services and update the server. It then reboots the server and closes the SSH connection.

from Server import Server
import paramiko

# Prints name of the script and it's author.
def print_program_info():
    print("Server Automator v0.1 by Nicholas McLendon")

# Connects to my EC2 server.
def connect_to_ec2(ec2Server):
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Owner\Documents\Schoolwork\CNE335\AWSproject\CNE335-NicholasMcLendon-F23-NicholasMcLendon-EC2forFinal.pem')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ec2Server, username='ubuntu', pkey=key)
    return ssh, ec2Server

# Install MySQL, and Apache. Can be expanded upon to install any service you want.
def add_services(ssh):
    commands = 'sudo apt install -y mysql-server && sudo apt install -y apache2'
    execute_command(ssh, commands)

# Fetches updates for server and upgrades Ubuntu.
def update_server(ssh):
    commands = 'sudo apt update && sudo apt upgrade -y && sudo apt autoremove && sudo apt autoclean'
    execute_command(ssh, commands)

# Fetches updates for services and upgrades them.
def update_services(ssh):
    commands = 'sudo apt update && sudo apt upgrade -y mysql-server && sudo apt upgrade -y apache2'
    execute_command(ssh, commands)

# Executes commands in my Ubuntu server terminal.
def execute_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    for line in stdout:
        print(line.strip())

# Pings a server.
def ping_request(server):
    request = server.ping()
    print(request)

def restart_server(ssh):
    command = 'sudo reboot'
    execute_command(ssh, command)
    print('Rebooting Server.')

# Main body of code.
def main():
    try:
        # Print infor and create Server object.
        print_program_info()
        ec2Server = Server('34.218.242.192')

        # Ping server to make sure it is running and reachable.
        ping_request(ec2Server)

        # Connect to server and update Ubuntu.
        ssh, ec2Server = connect_to_ec2(ec2Server.server_ip)
        update_server(ssh)

        # Install additional services and update them.
        add_services(ssh)
        update_services(ssh)

        # Reboots server.
        restart_server(ssh)

    # Handles errors and provides information.
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Closes SSH connection.
    ssh.close()

if __name__ == '__main__':
    main()