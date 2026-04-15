import socket
import threading
import tkinter as tk
root=tk.Tk()
root.title("Port Scanner")
root.geometry("400x300")
label=tk.Label(root, text="Target: ")
label.pack()
entry=tk.Entry(root)
entry.pack()
label=tk.Label(root, text="Start Port: ")
label.pack()
entry2=tk.Entry(root)
entry2.pack()
label=tk.Label(root, text="End Port: ")
label.pack()
entry3=tk.Entry(root)
entry3.pack()
output=tk.Text(root, height=10, width=40)
output.pack()

def start_scan():
    target = entry.get()
    start = int(entry2.get())
    end = int(entry3.get())
    ports = range(start, end+1)
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Scanning {target} from port {start} to {end}...\n")
    output.see(tk.END)
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)
button=tk.Button(root, text="Scan", command=start_scan)
button.pack()

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    if result == 0:
       output.insert(tk.END, f"{target}:{port} is open\n")
       output.see(tk.END)
    s.close()

root.mainloop()
