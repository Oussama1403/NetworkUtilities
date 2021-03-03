#install python-nmap module.
#install nmap https://nmap.org/.
#RUN AS SUDO TO OUTPUT MAC ADDRESS + Hostnames.
import nmap
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
#print("host",host)
s.close()
nm = nmap.PortScanner()
l = nm.scan(hosts = f'{host}/24', arguments = '-sn')
#print(l)
iplist = l['scan'].keys()
iplist = list(iplist)
for ip in iplist:
    V=[]
    try:
        ipinfo = l['scan'][ip]["addresses"]["mac"]
        try:
            vendor = l['scan'][ip]["vendor"]
            v = vendor[ipinfo]
            V.append(ip)
            V.append(ipinfo)
            V.append(v)
        except:
            V.append(ip)
            V.append(ipinfo)   
    except:
        V.append(ip)
    
    print(V)
