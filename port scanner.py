import socket
import threading
import tkinter as tk

#color theme variables

BG="#0f1117"
FG="#e2e4f0"
Entry_BG="#12141f"
ACTIVE_BG="#726bf2"
ACCENT="#6c63ff"
Muted="#8b8fa8"

#create main window
root=tk.Tk()
root.title("Port Scanner")
root.geometry("450x400")

#adding padding 
root.configure(bg=BG)
root.configure(padx=15, pady=15)

#congigure grid layout and columns to expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

#header frame with title and status
frame=tk.Frame(root, bg=BG)

#allow streching 
frame.grid_columnconfigure(0,weight=1)

#place headers across both columns 
frame.grid(row=0, column=0,columnspan=2, sticky="ew", pady=10)

#title label left side
title=tk.Label(frame, text="⬡ Port Scanner", bg=BG, fg=FG, font=("Segoe UI", 16, "bold"))
title.pack(side="left")

#status label right side
status=tk.Label(frame, text="Idle •", font=("Segoe UI", 10), bg=BG, fg=Muted)
status.pack(side="right")

#Inputs 


tk.Label(root, text="Target: ", bg=BG, fg=FG).grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry=tk.Entry(root,bg=Entry_BG, fg=FG, insertbackground=FG)
entry.grid(row=1, column=1, padx=8, pady=8)

tk.Label(root, text="Start Port: ", bg=BG, fg=FG).grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry2=tk.Entry(root,bg=BG, fg=FG, insertbackground=FG)
entry2.grid(row=2, column=1, padx=8, pady=8)

tk.Label(root, text="End Port: ", bg=BG, fg=FG).grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry3=tk.Entry(root, bg=Entry_BG, fg=FG, insertbackground=FG)
entry3.grid(row=3, column=1, padx=8, pady=8)

scrollbar=tk.Scrollbar(
    root,
    bg=BG,
    troughcolor=Entry_BG,
    activebackground=ACCENT,
)

output=tk.Text(root,font=("consolas", 10),
     bg=Entry_BG, fg=FG, insertbackground=FG, height=10, width=45, yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)
output.grid(row=5,column=0, columnspan=2,pady=10 )
scrollbar.grid(row=5, column=2, sticky="ns")
output.see(tk.END)

#list to store open ports found during scan
open_ports=[]

#runs scan in different thread to avoid freezing the GUI
def run_scan():
    start_scan()
   

#the main scan function that updates the status and output
def start_scan():
    status.config(text="Scanning •••", fg=ACCENT)
    target = entry.get()
    start = int(entry2.get())
    end = int(entry3.get())
    ports = range(start, end+1)
    open_ports.clear()
    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Scanning {target} from port {start} to {end}...\n")
    output.see(tk.END)
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    for port in open_ports:
        output.insert(tk.END, f"{target}:{port} is open\n")
        output.see(tk.END)
    status.config(text=f"Done ({len(open_ports)} open)", fg="green")
    output.config(state="disabled")

button=tk.Button(root, text="SCAN", bg=ACCENT, fg="white",font=("Arial", 10),
     relief="flat",bd=0,activebackground=ACTIVE_BG, cursor="hand2", width=20,
     command=lambda: threading.Thread(target=run_scan).start())
button.grid(row=4, column=0, columnspan=2, pady=12)

#port scanning function that checks if a port is open and updates the open_ports list
def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, port))
    #if connection is successful > port is open
    if result == 0:
       open_ports.append(port)
    s.close()
#start the gui loop
root.mainloop()
