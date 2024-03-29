import sys
import os
import io
from nessrest import ness6rest
import argparse



nessus_url = "https://localhost:8834/"
login = "username";
password = "password";

# Handle arguments
parser = argparse.ArgumentParser()
parser.add_argument('--target',  required=True)
parser.add_argument('--policy', required=True)
parser.add_argument('--name', required=True)
parser.add_argument('--insecure', action="store_true")
parser.add_argument('--ca_bundle')
args = parser.parse_args()

# Log in
scan = ness6rest.Scanner(url=nessus_url, login=login, password=password, insecure=args.insecure, ca_bundle=args.ca_bundle)

# Set policy that should be used
scan.policy_set(name=args.policy)

# Set target and scan name
scan.scan_add(targets=args.target, name=args.name)

# Run scan
scan.scan_run()


# Extract Scan results
scan.scan_results()
