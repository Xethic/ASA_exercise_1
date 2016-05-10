import sys

def horspool_preprocessing( sigma , P ):
	shifts = dict()
	for c in sigma :
		shifts [ c ] = len( P ) + 1
	for i in range( len( P ) ):
		shifts[ P [ i ]] = len( P ) - i
	return shifts

def horspool_matching( sigma , P , T ):
	shifts = horspool_preprocessing( sigma , P )
	print str(shifts)
	i = len( P ) - 1
	while i < len( T ):
		if T [i - len( P )+1: i +1] == P :
			yield i
		if i+1 >= len( T ):
			break;
		i += shifts[ T [ i + 1]]

sigma = ['A', 'C', 'G', 'T']

args = sys.argv
pattern = args[1]
f = open(args[2], 'r')

text = ''
for line in f:
	line = line.replace('\n', '')
	text += line

f.close()

indizes = horspool_matching(sigma, pattern, text)
output = ''
for index in indizes:
	output += str(index) + ','
print output[:-1]
