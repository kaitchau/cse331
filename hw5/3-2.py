import dpkt

def analyze_pcap(pcap_file):
    ipv4_count = 0
    non_ipv4_count = 0
    first_timestamp = None
    last_timestamp = None
    total_packets = 0

    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)

        for timestamp, buf in pcap:
            # Update first and last timestamps
            if first_timestamp is None:
                first_timestamp = timestamp
            last_timestamp = timestamp

            # Parse the Ethernet frame
            eth = dpkt.ethernet.Ethernet(buf)
            total_packets += 1

            # Check for IPv4 packets
            if isinstance(eth.data, dpkt.ip.IP):
                ipv4_count += 1
            else:
                non_ipv4_count += 1

    # Calculate metrics
    if first_timestamp:
        first_timestamp_str = "{:.2f}".format(first_timestamp)
    else:
        first_timestamp_str = "N/A"
    avg_packet_rate = (
        total_packets / (last_timestamp - first_timestamp)
        if first_timestamp and last_timestamp and (last_timestamp > first_timestamp)
        else 0.0
    )

    # Print results
    print("IPv4 count: {}".format(ipv4_count))
    print("Non-IPv4 count: {}".format(non_ipv4_count))
    print("First timestamp: {}".format(first_timestamp_str))
    print("Avg packet rate: {:.2f}".format(avg_packet_rate))

# Run the analysis on the PCAP file
analyze_pcap('trace2.pcap')
