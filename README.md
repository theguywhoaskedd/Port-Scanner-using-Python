# Python GUI Port Scanner

A fast, multithreaded **port scanner with a graphical interface** built using Python.

---
# Screenshot

<img width="556" height="534" alt="image" src="https://github.com/user-attachments/assets/95f3958d-932d-4e8d-9261-c91d3831eeb8" />


## Features

* Simple GUI (Tkinter)
* CLI version for terminal usage
* Scan any IP address or domain
* Custom port range input
* Multithreaded scanning (fast performance)
* Live results displayed in GUI

---

## Technologies Used

* Python
* socket (network connections)
* threading (parallel scanning)
* tkinter (GUI)

---

## How to Run
* CLI:

* .Clone the repository
* .Run the script:

```bash
python port_scanner.py
```

---

* GUI:
1. Clone this repository:

```bash
git clone https://github.com/your-username/python-port-scanner.git
```

2. Navigate to the folder:

```bash
cd python-port-scanner
```

3. Run the program:

```bash
python port_scanner_gui.py
```

---

## Usage

1. Enter a target:

   * IP address (e.g., `192.168.1.1`)
   * or domain (e.g., `google.com`)

2. Enter:

   * Start port
   * End port

3. Click **Scan**

4. View results in the output box

---

## Example Output

<img width="556" height="534" alt="image" src="https://github.com/user-attachments/assets/55836349-0c89-4d91-9247-0afbe83669e7" />


```
Scanning google.com from port 22 to 100...
google.com:53 is open
google.com:80 is open
```



