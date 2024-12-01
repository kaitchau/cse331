import dpkt

with open('trace2.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    snap_len = pcap.snaplen
    print("Snap Length: {}".format(snap_len))
