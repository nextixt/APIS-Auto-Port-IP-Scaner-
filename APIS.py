import pyfiglet
import sys
import socket
 
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
 
# Defining a target
if len(sys.argv):
    target_ip = sys.argv[2]
    mode = sys.argv[1]
else:
    print("Invalid amount of Argument")

try:
    if mode == "SINGLE":
        target_port = int(sys.argv[3])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip,target_port))
        if result == 0:
                print(f"Port {target_port} is open")
                s.close()
        else:
            print(f"Port {target_port} is closed")

    elif mode == "RANGE":
        start = int(sys.argv[3])
        stop = int(sys.argv[4])
        for port in range(start, stop + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip,port))
            if result == 0:
                print(f"Port {port} is open")
                s.close()
            else:
                print(f"Port {port} is closed")
              
        
except KeyboardInterrupt:
        print("\n Exiting Program...")
        sys.exit()
