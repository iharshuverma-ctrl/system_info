# System Information Tool

import platform
import os
import socket
from datetime import datetime

print("=" * 45)
print("       SYSTEM INFORMATION TOOL")
print("=" * 45)

# Operating System
print("\n🖥️ Operating System")
print("OS Name      :", platform.system())
print("OS Version   :", platform.version())
print("Architecture :", platform.machine())

# Computer Information
print("\n💻 Computer Information")
print("Computer Name:", socket.gethostname())
print("Processor    :", platform.processor())

# IP Address
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("IP Address   :", ip_address)

except socket.error:
    print("IP Address   : Unable to detect")

# Python Information
print("\n🐍 Python Information")
print("Python Version:", platform.python_version())

# Current User
print("\n👤 User Information")
print("Username:", os.getlogin())

# Current Time
print("\n🕒 Current Time")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("\n" + "=" * 45)
print("✅ Information collected successfully!")
print("=" * 45)
