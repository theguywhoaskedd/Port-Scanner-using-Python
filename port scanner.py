import socket
import threading
import tkinter as tk
root=tk.Tk()
root.title("Port Scanner")
root.geometry("450x350")
root.configure(padx=15, pady=15)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

label=tk.Label(root, text="Target: ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry=tk.Entry(root, width=25)
entry.grid(row=0, column=1, padx=5, pady=5)

label=tk.Label(root, text="Start Port: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry2=tk.Entry(root, width=25)
entry2.grid(row=1, column=1, padx=5, pady=5)

label=tk.Label(root, text="End Port: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry3=tk.Entry(root, width=25)
entry3.grid(row=2, column=1, padx=5, pady=5)

scrollbar=tk.Scrollbar(root)
output=tk.Text(root, height=10, width=45, yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)
output.grid(row=5,column=0, columnspan=2,pady=10 )
scrollbar.grid(row=5, column=2, sticky="ns")
output.see(tk.END)

def start_scan():
    target = entry.get()
    start = int(entry2.get())
    end = int(entry3.get())
    ports = range(start, end+1)
    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Scanning {target} from port {start} to {end}...\n")
    output.see(tk.END)
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)
button=tk.Button(root, text="Scan", width=20, command=start_scan)
button.grid(row=4, column=0, columnspan=2, pady=10)

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    if result == 0:
       output.insert(tk.END, f"{target}:{port} is open\n")
       output.see(tk.END)
       output.config(state="disabled")
    s.close()

root.mainloop()
