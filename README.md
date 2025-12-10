# LEGO Spike USB Serial Console


Send text lines from your PC to a LEGO® SPIKE™ hub over USB using Python and MicroPython paste mode.

This repo provides a small, focused script that:

- Interrupts any running program on the hub  
- Uploads a MicroPython “receiver” program using **paste mode**  
- Turns your PC terminal into a simple **line-based console** for the hub  
  (each line you type on the PC is sent over USB to the hub)

---

## ✨ Features

- 🧱 Works with LEGO® SPIKE™ (MicroPython over USB)  
- 🔌 Uses standard serial over USB (via pySerial)  
- ⌨️ Interactive: type lines on the PC, hub receives them via `sys.stdin`  
- 🔔 Hub beeps for each received line and prints an ACK  
- 🧪 Minimal, readable code — easy to customize for your own projects  

---

## 📁 Repository structure


```text
LEGO-Spike-USB-Serial-Console
├─ src/
│  └─ pc_spike_usb_communication.py
├─ LICENSE
├─ README.md
└─ requirements.txt
```

The core of the project is the `pc_spike_usb_communication.py` script in `src/`.

## 🧩 Requirements

- Python **3.8+** (any recent 3.x is fine)  
- pySerial 
- A LEGO® SPIKE™ hub connected to your PC via **USB**  
- Correct serial port configured in the script:  
  - Windows: something like `COM9`  
  - Linux: `/dev/ttyACM0`  
  - macOS: `/dev/tty.usbmodem*`  

---

## ⚙️ Installation

1. **Clone the repo**
```console
git clone https://github.com/ammardaher/LEGO-Spike-USB-Serial-Console

cd LEGO-Spike-USB-Serial-Console
```
2. **Create a virtual environment (optional but recommended)**
```console
virtualenv -p python3 .venv

source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```
3. **Install dependencies**
```console
pip install -r requirements.txt
```
---


## 🚀 Quick start

1. **Connect the SPIKE hub via USB** to your computer.  
2. Open `src/pc_send_to_spike_usb.py` and adjust the `PORT` constant if needed:
```python
   PORT = "COM9"        # Windows example. On Linux: /dev/ttyACM0 ; macOS: /dev/tty.usbmodem*
   
   BAUD = 115200
```
4. **Run the script:**
```console
   python src/pc_send_to_spike_usb.py
```
5. You should see something like:
```sh
   HUB: READY (send lines over USB)
   PC: Type lines to send. Ctrl+C to exit.
   > 
```
6. Type a line and press **Enter**:
```sh
   > hello SPIKE
   HUB: ACK -> hello SPIKE

   The hub will:  
   - Beep at 880 Hz for 120 ms  
   - Print `HUB: ACK -> hello SPIKE` back to your PC  
```
7. Press **Ctrl+C** on the PC side to exit:
```sh
   PC: Type lines to send. Ctrl+C to exit.
   > test
   HUB: ACK -> test
   ^C
   PC: Bye!
```
---

## 🔍 How it works

### 1. PC side — `pc_send_to_spike_usb.py`

The script uses `serial.Serial(PORT, BAUD, timeout=0.1)` to open the USB serial connection to the hub.

Key steps:

1. **Interrupt running program** (enter REPL):
```python
   ser.write(b'\x03')  # Ctrl-C
```
2. **Enter MicroPython paste mode**:
```python
   ser.write(b'\x05')  # Ctrl-E (paste mode)
```
3. **Paste the hub-side receiver program** (`HUB_PROGRAM`) and execute it:
```python
   ser.write(HUB_PROGRAM)
   ser.write(b'\x04')  # Ctrl-D to run pasted block
```
4. **Interactive loop**: read a line from the PC, send it to the hub, then read back whatever the hub printed:
```python
   while True:
       user_line = input("> ")
       ser.write(user_line.encode("utf-8") + b"\n")
       time.sleep(0.05)
       read_available(ser, 0.4)
```
`read_available(...)` is a helper that drains all available output from the hub for a short time and prints it to your PC console.

---

### 2. Hub side — receiver program

The script dynamically uploads and runs this MicroPython program on the hub:
```python
import sys, hub
print("HUB: READY (send lines over USB)")
while True:
    try:
        line = sys.stdin.readline()
        if not line:
            continue
        line = line.strip()
        if not line:
            continue
        hub.sound.beep(880, 120)
        print("HUB: ACK ->", line)
    except Exception as e:
        print("HUB: ERROR:", e)
```
What it does:

- Waits for a line from `sys.stdin` (i.e. from the PC over USB).  
- Ignores empty lines.  
- When a non-empty line arrives:  
  - Beeps  
  - Prints back `HUB: ACK -> <your line>`  

This makes a very simple **command channel** between your PC and the hub.

---

