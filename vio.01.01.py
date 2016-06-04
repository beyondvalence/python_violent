#! /usr/bin/python

# violent
# dictionaries

print('Services dictionary\n')
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
print('Services keys')
print(services.keys())

print('\nServices items')
print(services.items())

print('\nServices has \'ftp\' key')
print(services.has_key('ftp'))

print('\nValue of ftp key')
print(services['ftp'])

print('\n[+] Found vuln with FTP on port '+str(services['ftp'])+'\n')