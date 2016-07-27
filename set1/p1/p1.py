import string
import math

# defining base64 symbols
base64_symbols = list(string.ascii_uppercase) + list(string.ascii_lowercase) + [str(i) for i in xrange(10)]+ ["+","/"]

hex_num = raw_input()

# converting hex to bin
bin_num = bin(int(hex_num,16))[2:]

# calculating length of base64 number
len_bin_num = len(bin_num)
len_base64_num = int(math.ceil(float(len_bin_num)/6))

# padding binary string with initial zeros if necessary
padding = len_base64_num*6 - len_bin_num
bin_num = ['0' for i in xrange(padding)] + list(bin_num)

len_bin_num = len(bin_num)

# if len_base64_num != len_bin_num/6:
# 	print "Error in len_base64_num"
# 	exit()
# 	

base64_num = [0 for i in xrange(len_base64_num)]

# populating the base64_num in reverse order
for i in reversed(xrange(len_base64_num)):
	base64_num[i] = base64_symbols[int("".join(bin_num[i*6:i*6+6]),2)]

z = "".join(base64_num)
print z


# y = raw_input()
# if z != y:
# 	print "Failed"
# else:
# 	print "Success"