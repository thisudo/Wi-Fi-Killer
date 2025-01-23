# 🚀 Wi-Fi Killer - Deauthentication Script

## ⚡ What is it?

Wi-Fi Killer is a simple tool that lets you perform a **deauthentication attack** on Wi-Fi networks. 🛠️ It sends packets to disconnect devices from a target network (BSSID). Only use it on networks you own or have explicit permission to attack! 🚨

💥 **Warning**: This script is for **educational purposes only**! Misusing it could get you in legal trouble. 🏴‍☠️

---

## 🛠️ Features

- 🏙️ **Scan networks** and see their details (SSID, BSSID, channel, etc.)
- 💣 **Deauth attack**: Disconnect devices from a selected Wi-Fi network
- 🕵️‍♂️ **Anonymize your MAC** address for privacy
- 🔄 **Change channels** to target specific networks more easily
- 🚫 **Stop NetworkManager** to prevent automatic mode-switching

---

## 🔥 Requirements

Before you can use this script, you'll need to install some tools:

- aircrack-ng 🔐
- macchanger 🛡️
- iw 📡
- libncurses5-dev 🎮
- libpcap-dev 🕹️
- Python 3 + pip 🐍

You'll also need to install the `tabulate` library:

```bash
pip3 install tabulate
```
Get it up and running in just a few steps! 🎉

Clone the repo:
```bash
git clone https://github.com/thisudo/wifi-Deauthentication-script
cd wifi-Deauthentication-script
sudo install.sh
```
This will set up all your dependencies:

🏃‍♂️ Usage
Run the script:
```bash
sudo python3 wifi_killer.py
```
Pick your interface (e.g., wlan0).

Scan networks and pick the BSSID of the target you want to attack. 💥

Confirm the channel and start the attack. 💣

Hit Ctrl+C to stop the attack and clean everything up. 🔚

⚠️ Important Notes
Run as root: You need admin privileges to make this work. (sudo is your friend) 🧑‍💻
Be responsible: Don't mess with networks you don't own. 🚫
NetworkManager might try to reconnect your interface automatically. The script does its best to stop that! ⛔
Legal stuff: You're on your own here. Make sure you understand the laws in your country. 📜
📜 License
This script is licensed under the MIT License. Use it at your own risk! ⚠️

✍️ Author
Abdo3Dr
