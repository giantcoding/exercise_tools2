import socket, os, platform
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




# Main text
def main_menu():
    print("""
          
          Welcome human! What option do you want? Just write the corresponding number
          \n 1) Port checker    2) Get local IP and user name    3) Check OS name and version    4) Quit """ )


# Port checker, choice 1

def check_port():
    port = int(input("What port do you wanna check?: "))
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")
sock.close()

# IP Viever, choice 2

def check_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    local_name = socket.gethostname()
    user_name = username = os.getlogin()
    print('\n The local IP is: ' + local_ip, 'the name of localhost: ' + local_name + ' current PC user: ' + user_name)

# Os name and version, choice 3

def check_os():
    os_name = platform.system()
    os_version = platform.release()
    print('The OS name is: ' + os_name + ' running the version: ' + os_version)


