#To run the netdiscover tool from a Python script, you can use the subprocess module to execute the command. 
#First, ensure that netdiscover is installed on your system. Then, you can use the following Python code to run the tool:
#Make sure to replace "eth0" with the name of the network interface you want to use. Also, note that running network tools like netdiscover typically requires superuser privileges, so the script uses sudo to run the command. You may need to adjust the script and your system configuration accordingly.
#Remember to use this script responsibly and in compliance with any relevant laws and policies, as network scanning can raise legal and ethical considerations.



import subprocess

# Replace with the appropriate interface (e.g., eth0)
interface = "wlp2s0"

# Run netdiscover with the specified interface
try:
    subprocess.run(["sudo", "netdiscover", "-i", interface])
except FileNotFoundError:
    print("netdiscover command not found. Please make sure it's installed.")
except PermissionError:
    print("Permission denied. Make sure you have the necessary privileges to run netdiscover.")
