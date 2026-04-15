# Python GUI Port Scanner

A fast, multithreaded **port scanner with a graphical interface** built using Python.

---

## Features

* Simple GUI (Tkinter)
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

```
Scanning google.com from port 22 to 100...
google.com:53 is open
google.com:80 is open
```



