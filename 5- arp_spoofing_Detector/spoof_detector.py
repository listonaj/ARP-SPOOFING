# make sure you installed the module scapy <pip install scapy>
# Detecting ARP spoofing using a Python script and dsniff can be a bit more involved, 
# as it requires analyzing network traffic in real-time to identify suspicious ARP activity.
# One way to do this is by monitoring ARP traffic and checking for anomalies. 
# Below is a Python script that uses the Scapy library to help detect ARP spoofing:

import time
from scapy.all import ARP, Ether, sniff

# Define a dictionary to keep track of ARP cache mappings
arp_cache = {}

# Define a function to monitor ARP traffic
def monitor_arp():
    while True:
        try:
            # Sniff ARP packets on the network
            arp_packets = sniff(filter="arp", count=10)

            for packet in arp_packets:
                if ARP in packet:
                    arp_packet = packet[ARP]

                    # Extract the sender's IP and MAC address
                    sender_ip = arp_packet.psrc
                    sender_mac = arp_packet.hwsrc

                    # Check if the sender's IP address has been previously seen
                    if sender_ip in arp_cache:
                        # If the MAC address has changed, it's a sign of ARP spoofing
                        if arp_cache[sender_ip] != sender_mac:
                            print(f"ARP spoofing detected: {sender_ip} is at {sender_mac}, "
                                  f"but was previously at {arp_cache[sender_ip]}")

                    # Update the ARP cache
                    arp_cache[sender_ip] = sender_mac

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    try:
        # Start monitoring ARP traffic
        monitor_arp()
    except KeyboardInterrupt:
        print("ARP spoofing detection script terminated.")


### This script continuously monitors ARP traffic and maintains an ARP cache of known IP-to-MAC mappings. 
# If it detects a change in the MAC address associated with a known IP address, it raises an alert, as this could indicate ARP spoofing.
# Keep in mind that ARP spoofing detection is a complex task, and this script is a simple example. 
# For robust ARP spoofing detection in a production environment, you may want to consider more advanced solutions and intrusion detection systems. 
# Additionally, you should run this script with appropriate permissions (e.g., as a superuser) to capture network traffic effectively.