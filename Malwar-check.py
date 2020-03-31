#!/usr/bin/env python

import sys
import hashlib
import subprocess

if len(sys.argv) <1 :
  print("Usage Malware-check  <FILEPATH>")
  sys.exit(1)

file = sys.argv[1] 
B_SIZE = 65536 # The size of each read from the file

f_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        f_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

hash = f_hash.hexdigest() # Get the hexadecimal digest of the hash


#format 
#whois -h hash.cymru.com 2d23ca7b0b1d8869c8031ee0f03a2e19
output = subprocess.check_output(["whois", "-h", "hash.cymru" ,hash ] )

print(output)
