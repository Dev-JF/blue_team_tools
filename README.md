# blue_team_tools
Blue Team Scripts to help automate network protection



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


  ## Tool 2: Nessus local network scan
