import sipfullproxy
import socket
import logging
import sys
import socketserver

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy_call_log.log', level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

ipaddress = str()

q = input("A - pre automaticke ziskanie IP adresy\nLubovolna klavesa - pre manualne zadanie IP adresy\n")

if q == 'A' or q == 'a':
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
else:
    ipaddress = input("Zadajte IP adresu servera: ")

print('IP Adresa SIP servera: ' + ipaddress)

sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)
server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
server.serve_forever()
