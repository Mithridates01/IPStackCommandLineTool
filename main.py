import os
import re
import sys
import json
import logging
import argparse
from ipstack_api import IPStackAPI

def valid_ip(ip_str):
    # Regular expression for matching IPv4 addresses
    ipv4_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    ips = ip_str.split(',')

    for ip in ips:
        if not re.match(ipv4_regex, ip):
            raise argparse.ArgumentTypeError(f"'{ip}' is not a valid IPv4 address.")

    return ips

def cmd_line_interface():
  parser = argparse.ArgumentParser(description="IPStack CLI tool for IP address geo-location")
  parser.add_argument("--locate_ips", 
                      help="IP address(es) to query, comma-separated if multiple. Validated for single or comma delinated list of IPv4 addresses",
                      metavar='IPs', type=valid_ip)
  parser.add_argument("--full",
                      action='store_true',
                      help="Output in full details in JSON format")
  args = parser.parse_args()

  if not os.environ.get('IPSTACKACCESSKEY'):
    # Implement logic to save the access key in a secure place
    os.environ['IPSTACKACCESSKEY'] = f'{args.set_access_key}'
    print(f"Access key set to environment variable IPSTACKACCESSKEY")
    sys.exit()
  
  # Fetch the access key from environment variable or set_access_key argument
  access_key = os.environ.get('IPSTACKACCESSKEY')
  args.access_key = access_key

  if not access_key:
    print("The API access key is missing. Please set it with terminal command export IPSTACKACCESSKEY='access_key'.")
    sys.exit()

  if not args.locate_ips:
    print("No IP address provided. Please provide an IP address with --locate_ips")
    sys.exit()

  return args
