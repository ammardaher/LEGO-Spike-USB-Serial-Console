import sys
import time
import serial

PORT = "COM9"        # Windows example. On Linux: /dev/ttyACM0 ; macOS: /dev/tty.usbmodem*
BAUD = 115200

HUB_PROGRAM = br'''
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
'''

def read_available(ser, timeout=0.2):
    """Drain whatever the hub has printed so far."""
    end = time.time() + timeout
    out = b""
    while time.time() < end:
        chunk = ser.read(ser.in_waiting or 1)
        if not chunk:
            time.sleep(0.01)
            continue
        out += chunk
    if out:
        try:
            sys.stdout.write(out.decode("utf-8", errors="ignore"))
        except Exception:
            pass

with serial.Serial(PORT, BAUD, timeout=0.1) as ser:

    # 1) Interrupt any running program -> REPL
    ser.write(b'\x03')  # Ctrl-C
    time.sleep(0.2)
    read_available(ser, 0.3)

    # 2) Enter paste mode
    ser.write(b'\x05')  # Ctrl-E (paste mode)
    time.sleep(0.1)

    # 3) Paste the hub receiver program
    ser.write(HUB_PROGRAM)
    time.sleep(0.05)

    # 4) Finish paste (execute)
    ser.write(b'\x04')  # Ctrl-D to run pasted block
    time.sleep(0.2)
    read_available(ser, 0.6)
    print("PC: Type lines to send. Ctrl+C to exit.")
    try:
        while True:
            user_line = input("> ")
            # Send the line followed by newline so the hub's readline() returns
            ser.write(user_line.encode("utf-8") + b"\n")
            #ser.write('amaa\n'.encode())
            # Read hub's ACK
            time.sleep(0.05)
            read_available(ser, 0.4)
    except KeyboardInterrupt:
        print("\nPC: Bye!")
