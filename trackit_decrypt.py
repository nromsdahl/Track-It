#!/usr/bin/python3
#requires PyCryptodome
#based on blog https://gracefulsecurity.com/bmc-numara-track-it-decrypt-pass-tool/, updated for python3
#test encyrpted string, decrypts to password: Dhs0+pZA8VM=
#Usage:  Python3 trackit_decrypt.py Dhs0+pZA8VM=

import base64
import sys
from Crypto.Cipher import DES

encoded_ciph = sys.argv[1]
cipher_text = base64.b64decode(encoded_ciph)
cipher = DES.new('NumaraTI'.encode("utf8"), DES.MODE_CBC, 'NumaraTI'.encode("utf8"))
print(cipher.decrypt(cipher_text))
