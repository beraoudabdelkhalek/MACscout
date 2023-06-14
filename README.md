# MACscout
a Python tool for performing many lookup types related to MAC addresses, without an internet connection.
#Features
- finding the vendor name using a MAC address or using  MAC address block types
- finding the OUI of a vendor
- generating random MAC addresses or valid random MAC addresses by concatenating an existing OUI with a random individual address
#Usage
 use the following command to get the list of commands:
 '''
 python scout.py -h
 or use
 '''
 ./scout.py -h
- example:
  '''
  ./scout.py -m 00:01:4A:44:8C:7E
  Sony Corporation
  
