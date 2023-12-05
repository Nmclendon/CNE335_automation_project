
# Server Automator

# Introduction
This script, is designed to automate various tasks on an Ubuntu server, specifically an EC2 instance in AWS. The script is authored by Nicholas McLendon for his CNE 335 class and is currently at version 0.1.

# Dependencies
Before using the script, make sure you have the following dependencies installed:

paramiko: This library is used for SSH connections and is required for the script to communicate with the server.

# Script Structure
The script is organized into several functions.

1. print_program_info()
This function simply prints the name of the script and the author.

2. connect_to_ec2(ec2Server)
Establishes an SSH connection to the EC2 server specified by the ec2Server parameter, this parameter should be the IP address for your desired server.  It uses the Paramiko library to handle the SSH connection and authentication with a private key file.

3. add_services(ssh)
Installs MySQL and Apache on the connected server. This function can be extended to install additional services by modifying the commands variable accordingly.

4. update_server(ssh)
Fetches updates for the server's packages and upgrades the Ubuntu distribution.

5. update_services(ssh)
Fetches updates for installed services (MySQL and Apache in this case) and upgrades them.

6. execute_command(ssh, command)
Executes a specified command on the connected server. This function is utilized by other functions in the script.

7. ping_request(server)
Pings the server using the ping() method of a Server object. The server's response is then printed.

8. restart_server(ssh)
Issues a command to reboot the server.

9. main()
The main function executes the script. It prints information, creates a Server object, pings the server, establishes a connection, updates the server and services, and finally reboots the server.

# Usage
To use the script, follow these steps:

Ensure that the required dependencies are installed (paramiko).

Update the script with your own EC2 server IP in the main() function.

Run the script.

# Error Handling
The script includes a basic error-handling mechanism to catch exceptions and print error messages. If any error occurs during the execution, it will be displayed with relevant information.

# Suggestions for Improvement
Configuration File: Consider using a configuration file to store sensitive information such as server IP and private key file path, making the script more modular and secure.

Logging: Implement a logging mechanism to record events and errors, providing a detailed history of script executions.
