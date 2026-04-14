import socket
import threading
target=input("enter the ip or domain: ")
start=int(input("start port: "))
end=int(input("end port: "))
ports=range(start, end+1)
def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    if result == 0:
       print(f"{target}:{port} is open")
    s.close()
print(f"Scanning {target} from port {start} to {end}...")
threads=[]
for port in ports:
   t=threading.Thread(target=scan_port, args=(target, port))
   t.start()
   threads.append(t)
for t in threads:
   t.join()
