from scapy.all import sniff

def kuva_pakett(pkt):
    print(pkt.summary())

sniff(count=10, prn=kuva_pakett)
