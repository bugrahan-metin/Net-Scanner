import scapy.all as scapy
import optparse

# 1- ARP request
# 2- Broadcast
# 3- Response

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("--ip", dest="ip", help ="Enter IP address")
    (user_input,arguments) =  parse_object.parse_args()

    if not user_input.ip:
        print("Please enter IP address")
    return user_input.ip

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

ip = get_user_input()
scan_my_network(ip)





