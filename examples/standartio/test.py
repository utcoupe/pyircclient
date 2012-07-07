#!/usr/bin/python3

"""
	Simple echo program
"""

import time
import sys

print("echo script launched !")

while True:
	try:
		m = input()
	except Exception as ex:
		print(ex)
	else:
		print(m)
		continue
	break
	time.sleep(0.1)
