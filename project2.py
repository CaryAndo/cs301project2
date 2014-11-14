table = []

def setup_table():
	theFile = open('input.txt', 'r')
	for enum, line in enumerate(theFile):
		line = line.replace('\n', '')
		tony = line.split(' ')
		table.append([])

		for i, number in enumerate(tony):
			table[enum].append(float(number))

if __name__ == '__main__':
	setup_table()
	#print "Hello World!"
