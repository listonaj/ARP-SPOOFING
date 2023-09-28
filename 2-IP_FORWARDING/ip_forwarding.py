# Enabling IP forwarding on an Ubuntu machine allows it to act as a router and forward packets on behalf of other devices. 
# To enable IP forwarding, you can use the following Python code to execute the necessary commands via the subprocess module:
# Save this code in a Python file, and you can use it to enable or disable IP forwarding on your Ubuntu machine by uncommenting the appropriate lines. 
# Remember to run this script with superuser privileges (e.g., using sudo python script.py), 
# as enabling IP forwarding requires administrative access. 
# Also, be cautious when enabling IP forwarding, as it can impact the security of your network.

import subprocess

# Enable IP forwarding
def enable_ip_forwarding():
    try:
        # Enable IP forwarding in sysctl
        subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"], check=True)

        # Update iptables to allow packet forwarding
        subprocess.run(["iptables", "-A", "FORWARD", "-j", "ACCEPT"], check=True)

        print("IP forwarding is enabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Disable IP forwarding
def disable_ip_forwarding():
    try:
        # Disable IP forwarding in sysctl
        subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=0"], check=True)

        # Remove the FORWARD rule in iptables
        subprocess.run(["iptables", "-D", "FORWARD", "-j", "ACCEPT"], check=True)

        print("IP forwarding is disabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Enable or disable IP forwarding as needed
enable_ip_forwarding()  # Uncomment this line to enable IP forwarding

# To disable IP forwarding, uncomment the following line:
# disable_ip_forwarding()
