#!/bin/bash

# Display Wi-Fi Killer Banner
echo -e "\033[1;32m"
echo """
██╗    ██╗██╗      ███████╗██╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██║    ██║██║      ██╔════╝██║    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗█████╗  ██║    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██║███╗██║██║╚════╝██╔══╝  ██║    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║      ██║     ██║    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝      ╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                       by:thisudo
"""
echo -e "\033[0m"
echo -e "\033[1;34m[!] Wi-Fi Deauthentication Script [!]\033[0m"
echo -e "\033[1;33mFor educational purposes only!\033[0m"
echo -e "\033[1;33mUse at your own risk on your own network!\033[0m"
echo -e "\033[1;31mI am not responsible for any misuse!\033[0m"
echo ""

# Update system and install necessary tools
echo "[*] Installing dependencies..."

# Update system and install necessary tools
sudo apt update && sudo apt upgrade -y
sudo apt install -y aircrack-ng macchanger iw libncurses5-dev libpcap-dev python3-pip

# Install Python libraries
pip3 install tabulate

# Give execute permission
chmod +x wifi_killer.py

echo "[+] Installation complete. Run the script with: python3 wi-fi_killer.py"
clear
