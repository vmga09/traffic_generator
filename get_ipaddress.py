import ipaddress

def get_ipaddress(segmento):
    try:
        addr4 = ipaddress.ip_network(segmento, strict=False)
    except ValueError as e:
        return ["error"]
    else:
        if addr4.version == 4:
            network = ipaddress.IPv4Network(segmento)
            list_ip = [str(x) for x in network.hosts() ]
            return list_ip

