z = hex(int(raw_input(),16) ^ int(raw_input(),16))[2:-1]

print z

if z != raw_input():
	print "Failed"
else:
	print "Success"