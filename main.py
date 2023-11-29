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

def main():
  logging.basicConfig(level=logging.INFO)
  
  cmd_args = cmd_line_interface()

  ipstack_api = IPStackAPI(cmd_args.access_key)
  # TODO: IP list validation is done in arg parse type setting. 
  #   May be better to validate each and ips that aren't valid 
  #   provide feedback in console to user like:
  #   # out of # IPs were invalid return defective ips 10 per line
  ips = [ip.strip() for ip in cmd_args.locate_ips]
  
  if len(ips) > 1:
    bulk_ip_lookup_response = ipstack_api.ipstack_bulk_ip_location_lookup(ips)
    # TODO: Implement with paid API features.
    print(bulk_ip_lookup_response["error"]["info"])
    sys.exit()

    # Return dict of {"ip": "location"} or {"ip": {...location_details...}} if --full
    if cmd_args.full:
      bulk_ip_lookup_response = {obj["ip"]: obj for obj in bulk_ip_lookup_response}
      print(json.dumps(bulk_ip_lookup_response))
    else:
      bulk_ip_lookup_response = {obj["ip"]: ('(' + obj['longitude'] + ',' + obj['latitude']+')') for obj in bulk_ip_lookup_response}
      print(json.dumps(bulk_ip_lookup_response))
  else:
    single_ip_lookup_response = ipstack_api.ipstack_ip_location_lookup(ips[0])
    
    # Return dict of {"ip": "location"} or {"ip": {...location_details...}} if --full
    if cmd_args.full:
      print(json.dumps({single_ip_lookup_response["ip"]: single_ip_lookup_response}))
    else:
      gps_coordinates = "("+ str(single_ip_lookup_response["latitude"]) + "," + str(single_ip_lookup_response["longitude"]) + ")"
      print(f"{gps_coordinates}")



if __name__ == "__main__":
    main()