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
