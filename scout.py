import sys
import json
import re
import random


#the database is from this website: https://maclookup.app/
file = open("./mac-vendors.json", encoding="utf8")
data = json.load(file)


def generate_mac_address():
    mac_address = [random.randint(0x00, 0xff) for _ in range(6)]
    mac_address_str = ':'.join(['{:02X}'.format(byte) for byte in mac_address])
    return mac_address_str

#concatenate an existing OUI with a random individual address to get a valid mac address
def generate_mac_address_valid():
    mac_address = [random.randint(0x00, 0xff) for _ in range(3)]
    mac_address_str = ':'.join(['{:02X}'.format(byte) for byte in mac_address])
    random.shuffle(data)
    for element in data:
        if element["blockType"]=="MA-L": 
            return element["macPrefix"]+":"+mac_address_str


def is_valid_mac_address(mac_address):
    regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return regex.match(mac_address) is not None

def is_valid_oui(oui):
    regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){2}([0-9A-Fa-f]{2})$')
    return regex.match(oui) is not None

#get the vendor name from the max using a complete mac address or just the OUI
def getVendor(mac):
    macadr=mac.upper()
    if is_valid_mac_address(macadr) or is_valid_oui(macadr):
        for element in data:
            if element["macPrefix"]==macadr[0:8]:
                return element["vendorName"]
        return "vendor not found"
    else: return "invalid input"

#get the vendor name using MAC address blocks
def getVendorStrict(mac):
    macadr=mac.upper()
    for element in data:
        if element["macPrefix"]==macadr:
            return element["vendorName"]
    return "not found"

def getMACPrefixVendor(vendor):
    for element in data:
        if element["vendorName"].lower()==vendor.lower():
            return element["macPrefix"]
    return "not found"

listargs=sys.argv

if len(listargs)>1:
    if listargs[1]=="-h":
        print("\nuse the following:\n-h: show list of parameters\n-m [MAC address or OUI]: get the vendor name from the specified MAC adress or OUI\n-v [\"vendor name\"]: get the OUI from the vendor name\n-vs [MAC address block]: get the vendor name using any MAC address block type\n-g: generate a random MAC address\n-gv: get a mac address composed of an existing OUI and a random individual address")
    elif listargs[1]=="-m":
        print(getVendor(listargs[2]))
    elif listargs[1]=="-v":
        print(getMACPrefixVendor(listargs[2]))
        print(listargs[2])
    elif listargs[1]=="-vs":
        print(getVendorStrict(listargs[2]))
    elif listargs[1]=="-g":
        print(generate_mac_address())
    elif listargs[1]=="-gv":
        print(generate_mac_address_valid())
else: print("\nMACscout by Abdelkhalek Beraoud(letmewin)\n\nuse -h for help")

file.close()
    


