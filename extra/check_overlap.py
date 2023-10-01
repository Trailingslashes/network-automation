#!/usr/bin/env python3

import argparse
import ipaddress

def check_overlap(ip1, ip2):
    n1 = ipaddress.ip_network(ip1, strict=False)
    n2 = ipaddress.ip_network(ip2, strict=False)
    
    return n1.overlaps(n2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if two IP networks overlap")
    parser.add_argument("ip1", help="First IP network (e.g., '192.168.1.0/24')")
    parser.add_argument("ip2", help="Second IP network (e.g., '192.168.2.0/24')")
    args = parser.parse_args()
    
    result = check_overlap(args.ip1, args.ip2)
    if result:
        print(f"{args.ip1} overlaps with {args.ip2}")
    else:
        print(f"{args.ip1} does not overlap with {args.ip2}")
