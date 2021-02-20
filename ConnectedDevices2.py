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
ip = l['scan'].keys()
ip = list(ip)
for e in ip:
    try:
        ipinfo = l['scan'][e]["addresses"]["mac"]
        print(e,":",ipinfo)
    except:
        print("no mac")     
