# blue_team_tools
Blue Team Scripts to help network protection



## Tool 1: Shodan IP Check

requires: Shodan membership, shodan api key, shodan python package

Objective: To review internet facing services to ensure they are not vulnerable or are at an acceptable level i.e port 80 is open.

Overview:

Loops over a list of IPs in a json file, returns a list of:

- open ports
- product (if applicable)
- OS type (if applicable)
- CVEs shodan has identified

  Places the results in a Json file

  current state:

  is only checking one IP address, still requires:

  - json file to read ip
  - loop over IPs
  - export results to a json file


## Tool 2: Malicous IP/ URL checker - Under development

requires: 

Objective: utlises API to verify the vlaidity of an URL or IP address to confirm if its known malicious URL or IP

Functions:

- input a list in json of url or ip
- run the code, wait for the response



## Tool 3: Scapy network scanning

Objective: To make a customisable packet captuirng/ network scanning tool. This allows the information gathering within a network (externally and internally) to help 
blue teams discover what areas in their network are exposed

requires: scapy python packet

This tool has a few functions including:
- a syn scan with set ports to scan with the ip address
- dns scan to validate dns information
- a traceroute scan
- Passive OS scan (the example used is a linux fingerprint)



