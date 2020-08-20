import os
import urllib
import json
import sys
os.system("clear")
os.system("figlet -f standard Website Scanner")
print
print "Author : Rahat Khan Tusar(RKT)"
print
print "Github : https://github.com/r3k4t "
print
print "Information : Scan your website for vulnerabilities and find website application vulnerabilities."
print
ip = raw_input("Enter IP or Domain :")
print
print "-"*60
print "### Ping ###"
print "-"*60
os.system("ping -c 4 {} ".format(ip))
print "-"*60
print "### Dns-Lookup ### "
print "-"*60
os.system("dig {} ".format(ip))
print "-"*60
print "### Ns-Lookup ###"
print "-"*60
os.system("nslookup {} ".format(ip))
print "-"*60
print "### Reverse-DNS-Lookup ###"
print "-"*60
os.system("dig -x {}".format(ip))
print "-"*60
print "### Port-Scan ### "
print "-"*60
os.system("nmap {}".format(ip)) 
print "-"*60
print "### Whois-Lookup ###  "
print "-"*60
os.system("whois {} ".format(ip))
print "-"*60
print "### Geo-IP ### "
print "-"*60
os.system("{}".format(ip))
url = 'http://ip-api.com/json/'
response = urllib.urlopen(url + ip)
data = response.read()
rkt = json.loads(data)
print data
print "-"*60
print "### Traceroute ### "
print "-"*60
os.system("traceroute {} ".format(ip))
print "-"*60
print "### Have a nice day.bye. ###"
print "-"*60


 

