# networkattacks
This python scripts contain two network attack DHCP Starvation and Syn Flood

  | ___ \          | |             |  \/  |(_)     | |                
  | |_/ /_   _   __| | _ __  __ _  | .  . | _  ___ | |__   _ __  __ _ 
  |    /| | | | / _` || '__|/ _` | | |\/| || |/ __|| '_ \ | '__|/ _` |
  | |\ \| |_| || (_| || |  | (_| | | |  | || |\__ \| | | || |  | (_| |
  \_| \_|\__,_| \__,_||_|   \__,_| \_|  |_/|_||___/|_| |_||_|   \__,_|

## What Is the DHCP Process?
A Dynamic Host Configuration Protocol server is responsible for issuing IP addresses to devices on its network. This is done through a series of packet exchanges between individual DHCP clients and DHCP servers. To understand how a DHCP starvation attack works, we should first understand the DHCP interaction fully.

A DHCP IP address allocation transaction depends on four types of packets: DISCOVER, OFFER, REQUEST, and ACKNOWLEDGEMENT. While all four of these basic (DORA) packets are important to the DHCP process, we'll be focusing most on DISCOVER packets.

When a PC boots up on the network, if it's a DHCP client, it's going to issue a DHCP DISCOVER packet. By doing so, that PC is effectively saying, "Hi, I'm new here! I'm looking for a Dynamic Host Configuration Protocol server that can issue me an IP address."

If you visualize a client on a network reaching a nearby server, you can imagine the server responding with an OFFER. And in that offer, it's going to offer an IP address that the client is allowed to use. That server is effectively replying with, "Welcome. I've got a lovely little spot at 10.123.0.1 I can offer you. Interested?"

Before we go on to the client's reply to that, we should mention that the DHCP server has a pool of addresses it can select from. On a /24-bit network, the max number of IP addresses that could be in a pool would be 254.

Additionally, it's very likely that a few of those addresses are saved for static router addresses and so forth. So the pool of available addresses the DHCP server can draw from may only be about 252 IP addresses. When it receives a DISCOVER packet, the DHCP server chooses one of its remaining IP addresses from its pool and reserves it for the new client.

The next step, after the OFFER packet is received by the client is to send a REQUEST back. That's essentially the client saying, "Yes, that sounds perfect. Could I please have exclusive rights to 10.123.0.1 while I'm here?"

The final step in the transaction is when the server sends an ACKNOWLEDGEMENT packet to the client and anyone else listening. This essentially says, "You're now using 10.123.0.1. If anyone needs to reach that client, they're parked at 10.123.0.1."

In a non-hostile arrangement, this DHCP arrangement is an efficient way to have clients pop on and off of networks and remain available and safe. But a DHCP starvation attack exploits this process.

## DHCP Starvation -
A DHCP starvation attack is a malicious digital attack that targets DHCP servers. During a DHCP attack, a hostile actor floods a DHCP server with bogus DISCOVER packets until the DHCP server exhausts its supply of IP addresses. Once that happens, the attacker can deny legitimate network users service, or even supply an alternate DHCP connection that leads to a Man-in-the-Middle (MITM) attack.

## What is a SYN flood attack?
A SYN flood (half-open attack) is a type of denial-of-service (DDoS) attack which aims to make a server unavailable to legitimate traffic by consuming all available server resources. By repeatedly sending initial connection request (SYN) packets, the attacker is able to overwhelm all available ports on a targeted server machine, causing the targeted device to respond to legitimate traffic sluggishly or not at all.

## How does a SYN flood attack work?
SYN flood attacks work by exploiting the handshake process of a TCP connection. Under normal conditions, TCP connection exhibits three distinct processes in order to make a connection.

1) First, the client sends a SYN packet to the server in order to initiate the connection.
2) The server then responds to that initial packet with a SYN/ACK packet, in order to acknowledge the communication.
3) Finally, the client returns an ACK packet to acknowledge the receipt of the packet from the server. After completing this sequence of packet sending and receiving, the TCP connection is open and able to send and receive data.
