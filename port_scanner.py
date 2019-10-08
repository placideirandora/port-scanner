# Import required modules
import sys
import socket
from datetime import datetime

# Exception handling
try:
    # Ask for a host to scan
    print('\n')
    remote_host_domain_name = raw_input("Type In A Remote Host To Scan: ")
    remote_host_ip_address = socket.gethostbyname(remote_host_domain_name)

    # Display information about the host to be scanned
    print('_' * 110)
    print('Scanning The Remote Host... ')
    print('Domain Name: {}'.format(remote_host_domain_name))
    print('IP Address: {}'.format(remote_host_ip_address))
    print('_' * 110)
    print('\n')

    # Record the scan initial time
    initialTime = datetime.now()

    # Scan all ports specified in the Port Range
    for port in range(1, 1025):
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_result = network_socket.connect_ex((remote_host_ip_address, port))
        if connection_result == 0:
            print('Port {}: Open'.format(port))
        network_socket.close()
except KeyboardInterrupt:
    print('\n')
    print('You Have Stopped The Scan.')
    sys.exit()
except socket.gaierror:
    print('\n')
    print('Hostname Could Not Be Resolved. Exiting...')
    sys.exit()


# Record the scan final time
finalTime = datetime.now()

# Display the information on the terminal
print('\n')
print('Scan Completed')
print('Started At: {}'.format(initialTime))
print('Finished At: {}'.format(finalTime))





