import dpkt
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def analyze_pcap(file_path):
    # Initialize variables
    protocol_counts = defaultdict(int)
    packet_sizes = []
    unique_sources = set()
    unique_destinations = set()
    source_bytes = defaultdict(int)
    source_packets = defaultdict(int)
    first_timestamp = None
    last_timestamp = None

    # Open and read pcap file
    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)

        for i, (ts, buf) in enumerate(pcap):
            if first_timestamp is None:
                first_timestamp = ts
            last_timestamp = ts

            eth = dpkt.ethernet.Ethernet(buf)
            packet_sizes.append(len(buf))

            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                protocol_counts[ip.p] += 1
                unique_sources.add(ip.src)
                unique_destinations.add(ip.dst)
                source_bytes[ip.src] += len(buf)
                source_packets[ip.src] += 1

            # Print progress for large files
            if i % 10000 == 0 and i > 0:
                print("Processed %d packets..." % i)

    # Calculate metrics
    duration = last_timestamp - first_timestamp if first_timestamp is not None else 0
    avg_packet_rate = len(packet_sizes) / duration if duration > 0 else 0

    # Results
    print("\nAnalysis Results:")
    print("Unique sources: %d" % len(unique_sources))
    print("Unique destinations: %d" % len(unique_destinations))
    print("First timestamp: %.2f" % first_timestamp if first_timestamp else "None")
    print("Average packet rate: %.2f packets/sec" % avg_packet_rate)

    # Top 5 protocols
    print("\nTop 5 Protocols:")
    protocol_names = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}
    for proto, count in sorted(protocol_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        name = protocol_names.get(proto, "Protocol %d" % proto)
        print("%s: %d" % (name, count))

   # Bar chart for protocol distribution 
#    protocol_labels = [protocol_names.get(proto, "Protocol %d" % proto) for proto, _ in top_protocols] 
#    protocol_values = [count for _, count in top_protocols] 
#    plt.bar(protocol_labels, protocol_values, color='skyblue') 
#    plt.title("Top 5 Protocols by Packet Count") 
#    plt.xlabel("Protocol") plt.ylabel("Packet Count") plt.show()

#     # Source with most bytes and packets
#     most_bytes_source = max(source_bytes, key=source_bytes.get)
#     most_packets_source = max(source_packets, key=source_packets.get)
#     print("\nSource with most bytes: %s (%d bytes)" % (most_bytes_source, source_bytes[most_bytes_source]))
#     print("Source with most packets: %s (%d packets)" % (most_packets_source, source_packets[most_packets_source]))

# Run the script
analyze_pcap('trace2.pcap')