# Nicholas McLendon
# CNE 335 Fall 2023
# Automate ping/SSH
from Server import Server
import paramiko

def print_program_info():
    print("Server Automator v0.1 by Nicholas McLendon"

# This is the entry point to our program
if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Owner\Documents\Schoolwork\CNE335\AWSproject\CNE335-NicholasMcLendon-F23-NicholasMcLendon-EC2forFinal.pem')
    ec2Server = Server('34.210.125.71')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='34.210.125.71', username='ubuntu', pkey=key)

    print_program_info()

    stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo-apt upgrade -y && sudo-apt autoremove && sudo apt autoclean')
    line = stdout.readline()

    while line:
        line = stdout.readline()
        print(line)

    ssh.close()

    request = ec2Server.ping()