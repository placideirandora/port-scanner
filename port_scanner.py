# Import required modules
import sys
import socket
from datetime import datetime

# Exception handling
try:
    # Ask for a host to scan
    print('\n')
    remote_host_domain_name = input("Type In A Remote Host To Scan: ")
    remote_host_ip_address = socket.gethostbyname(remote_host_domain_name)

    # Display information about the host to be scanned
    print('_' * 110)
    print('Scanning The Remote Host For Open Ports... ')
    print('Domain Name: {}'.format(remote_host_domain_name))
    print('IP Address: {}'.format(remote_host_ip_address))
    print('_' * 110)
    print('\n')

    # Record the scan initial time
    initial_time = datetime.now()

    # Scan all ports specified in the Port Range
    for port in range(1, 1025):
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_result = network_socket.connect_ex((remote_host_ip_address, port))
        if connection_result == 0:
            print('Port {}: Open'.format(port))
        else:
            print('Port {}: Closed'.format(port))
        network_socket.close()
except KeyboardInterrupt:
    # Record the scan final time
    final_time = datetime.now()

    print('\n')
    print('You Have Stopped The Scan.\n')
    print('Started At: {}'.format(initial_time))
    print('Finished At: {}'.format(final_time))
    print('\n')
    sys.exit()
except socket.gaierror:
    print('\n')
    print('Hostname Could Not Be Resolved. Exiting...')
    sys.exit()


# Record the scan final time
final_time = datetime.now()

# Display the information on the terminal
print('\n')
print('Port Scan Completed')
print('Started At: {}'.format(initial_time))
print('Finished At: {}'.format(final_time))





