#install python-nmap module.
#install nmap https://nmap.org/.
import nmap
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
#print("host",host)
s.close()
nm = nmap.PortScanner()
l = nm.scan(hosts = f'{host}/24', arguments = '-sn')
p = l['scan'].keys()
p = list(p)
for i in range(len(p)):
    print("IP",i,p[i])
