#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json, os

if __name__ == '__main__':
	data = []
	with open('dump_1.json') as f:
		for line in f:
			encoded = json.loads(line)["Item"]["compressed_value"]['B']

			command = "echo " + encoded + "| base64 -d | gunzip"			
			command1 = "ls"
			
			line = os.system(command)
			print(line)
	