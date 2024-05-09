from scapy.all import *
import time
import json
from get_ipaddress import get_ipaddress

#Load config network file
def read_network_conf():
        network_file = open('network.json')
        data = json.load(network_file)
        return data


#Get list ip traffic
def get_ip(listaddress):
        lst_ip = []
        for ip in listaddress:
                lst_add = get_ipaddress(ip)
                lst_ip.extend(lst_add)
        return lst_ip

#Main function traffic generator
def main():
        network_file = read_network_conf()
        dest_address = get_ip(network_file["dst_ip"])
        source_address = get_ip(network_file["src_ip"])
        ports = network_file["ports"]
        while True:
                dest = random.choice(dest_address)
                source = random.choice(source_address)
                dport = random.choice(ports)
                sport = random.randint(1024,65535)
                ip=IP(src=source,dst=dest)
                SYN=TCP(sport=sport, dport=dport, flags='S', seq=0)
                #print(ip.show())
                print(f"Enviando paquetes: {source}:{sport}  --->  {dest}:{dport}")
                SYNACK=send(ip/SYN)
                time.sleep(3)
        



if __name__ == "__main__":
        main()

