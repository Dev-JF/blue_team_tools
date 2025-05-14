import shodan
import json

iplist_json = open('iplist.json')

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)


data = json.load(iplist_json)

for item in data['ip_add']:

    ip = item["ip"]
    
    
    ip_info = api.host(ip)
    
    # Extract open ports information
    open_ports = ip_info.get('ports')
    product = ip_info.get('product')
    os = ip_info.get('os')
    vulns = ip_info.get('vulns')
   
   

    print("Open Ports:", open_ports)
    print("Product:", product)
    print("OS:", os)
    print("CVEs:", vulns)

   
    print(ip)
