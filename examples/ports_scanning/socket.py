import socket
from pprint import pprint


def check_if_port_isopen(ip_address: str, port: int):
    """
    Tries to connect to a port then return True if possible, if not returns False
    """
    try:
        socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        socket_object.connect((ip_address, port))
        return True
    except Exception as var:
        return False


def scan_all_ports(ip_address: str):
    """
    Scans all the ports using "check_if_port_isopen" and return a list of opened ports
    """
    data = []
    for i in range(65536):
        if check_if_port_isopen(ip_address, i):
            data.append(i)
    return data


def read_service(ip_address: str, port: int):
    """
    Try to connect to a port then read what was sent and return it, or else returns None if it can't connect
    """
    try:
        socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        socket_object.connect((ip_address, port))
        return socket_object.recv(4096)
    except Exception:
        return None


def scan_all_services(ip_address: str):
    """
    Scans all the ports using "read_service" and return a dictionary of ports with the detected service on them
    """
    data = {}
    for i in range(65536):

        service_data = read_service(ip_address, i)
        if service_data is not None:
            print("Port: ", i)
            print("Service:", service_data)
            data[i] = service_data
    return data
