from scapy.all import *

from pyp0f.database import DATABASE
from pyp0f.exceptions import PacketError
from pyp0f.fingerprint import fingerprint_http, fingerprint_mtu, fingerprint_tcp
from pyp0f.net.layers.tcp import TCPFlag
from pyp0f.net.scapy import ScapyIPv4, ScapyIPv6, ScapyPacket, ScapyTCP

DATABASE.load()


ports = [25,80,53,443,445,8080,8443]

# sends syn packet and expects an ack packet in response
def SynScan(host):
    ans,unans = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP.dport])



# set dns host ip, port and domain name to confirm dns exists 
def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans:
        print("Dns Server at %s"%host)




# tracerout function
def TraceRoute(host):
    ans,unans=sr(IP(dst=host,ttl=(1,10))/UDP(),verbose=0)
    if ans:
        for snd, rcv in ans:
            print(snd.ttl, rcv.src, snd.sent_time, rcv.time)


host = '8.8.8.8'





#p0f : Passive OS fingerprinting: using syn or syn + ack
def PassiveOSFingerprintTCP(packet: ScapyPacket) -> None:
    flags = TCPFlag(int(packet[ScapyTCP].flags))
    
    if flags in (TCPFlag.SYN, TCPFlag.SYN | TCPFlag.ACK):
        mtu_result = fingerprint_mtu(packet)
        tcp_result = fingerprint_tcp(packet)
        print(f"MTU fingerprint match: {mtu_result.match}")
        print(f"TCP fingerprint match: {tcp_result.match}")
    

# example usage
pck = IP(b'E\x00\x00<\x00\x00@\x008\x06N;?t\xf3a\xc0\xa8\x01\x03\x00P\xe5\xc0\xa3\xc4\x80\x9f\xe5\x94=\xab\xa0\x12\x16\xa0N\x07\x00\x00\x02\x04\x05\xb4\x04\x02\x08\n\x8d\x9d\x9d\xfa\x00\x17\x95e\x01\x03\x03\x05')

PassiveOSFingerprintTCP(pck) 


# function to send a upd Packet Scan for a novel/ Particular vuln i.e eternal blue (through port type) requires further research, as in other ways to detect, i.e packet contents, then needs testing