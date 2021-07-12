#!/usr/bin/python

import base64
import argparse
import random

print """
                                        __         ____
    ____  ____ _      _____  __________/ /_  ___  / / /
   / __ \/ __ \ | /| / / _ \/ ___/ ___/ __ \/ _ \/ / / 
  / /_/ / /_/ / |/ |/ /  __/ /  (__  ) / / /  __/ / /  
 / .___/\____/|__/|__/\___/_/  /____/_/ /_/\___/_/_/   
/_/____  __    ____                      __            
  / __ \/ /_  / __/_  ________________ _/ /____        
 / / / / __ \/ /_/ / / / ___/ ___/ __ `/ __/ _ \       
/ /_/ / /_/ / __/ /_/ (__  ) /__/ /_/ / /_/  __/       
\____/_.___/_/  \__,_/____/\___/\__,_/\__/\___/        
                                                       
                                                                           
"""
def xor(encoded,key):
        return ''.join(chr(ord(a) ^ key) for a in encoded)

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="Path to powershell script",type=str,dest='path',required=True)
parser.add_argument("-o","--output", help="Output of powershell obfuscate script",type=str,dest='output',required=True)
args = parser.parse_args()

path = args.path
output = args.output

f = open(path,'r')
content = f.read()
f.close()

print "[+]Generation of random encryption key"
key = random.randint(1,196)
print "[+]Encode in UTF-16LE"
encoded = content.encode("utf-16-le")
print "[+]Encrypt in XOR"
encoded = xor(encoded, key)
print "[+]Encode in Base64"
encoded = base64.b64encode(encoded)
print "[+]Your powershell is encoded : " + output


with open("/usr/local/bin/template.txt") as f:
        templateObfu = f.read()
        
templateObfu = templateObfu.replace("$$DATA$$", encoded)
templateObfu = templateObfu.replace("$$KEY$$", str(key))

m = open(output,"w")
m.write(templateObfu)
m.close()

