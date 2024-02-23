import shodan



SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)



ip_info = api.host('47.97.242.49')

 # Extract open ports information
open_ports = ip_info.get('ports')
product = ip_info.get('product')
os = ip_info.get('os')
vulns = ip_info.get('vulns')
   
   

print("Open Ports:", open_ports)
print("Product:", product)
print("OS:", os)
print("CVEs:", vulns)

