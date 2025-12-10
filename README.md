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
