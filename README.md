#Manx
Download, parse, and filter multiple blocklists and inject them directly into your dnsmasq or hosts configurations.
##Usage
There are several ways to configure this application to produce the requested output.
###Simple
All uses require a list of blocklist urls outlined in an external line-delimited text file.
```$ python main.py blocklist.txt```
###Whitelist
Similar to the blocklist file, a whitelist text file may be provided that contains urls to omit from the final blacklist. Use -w to comment out these urls, or -W to remove them from the list completely.
```$ python main.py -w whitelist.txt blocklist.txt```
###Output
Specify an output configuration file. This file is typically lead by some information about this application and a timestamp. By default, blacklist.conf is produced in the script directory.
```$ python main.py -o /etc/dnsmasq.d/blacklist.conf -w whitelist.txt blocklist.txt```
###Install
This feature is not yet implemented, but it will use the -i flag to test the output file, install into dnsmasq by replacing an existing configuration file, and restart dnsmasq. Root privileges will be required.
```# python main.py -i -W whitelist.txt blocklist.txt```
###Output Type
This feature is not yet implemented, but a flag will be introduced to specify if the output file should be dnsmasq or hosts or something else.