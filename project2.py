table = []


def setup_table():
    """ Set up the table that holds x/y values """
    the_file = open('input.txt', 'r')
    for enum, line in enumerate(the_file):
        line = line.replace('\n', '')
        tony = line.split(' ')
        table.append([])

        for i, number in enumerate(tony):
            table[enum].append(float(number))

def generate_div_table():
    """ Modify the table using the divided difference method """
    #print('The length of table 0 is: ' + str(len(table[0])))
    iter = 0 # Keep track of how many columns we've done
    # Iterate over every column past the first two
    for i in xrange(len(table[0]) - 1):
        col_index = 1 + i
        iter += 1
        fin = []
        for j in xrange(len(table[0]) - iter):
            x0 = j
            x1 = x0 + (iter)
            f0 = j
            f1 = f0 + 1
            print('iter = ' + str(iter))
            print('x0: ' + str(x0) + ' x1: '+ str(x1))
            print('f0: ' + str(f0) + ' f1: '+ str(f1))
            print('col index = ' + str(col_index))
            print('Value f1 = ' + str(table[col_index-2][f1]))
            print('Value f0 = ' + str(table[col_index-2][f0]))
            print('Value x1 = ' + str(table[0][x1]))
            print('Value x0 = ' + str(table[0][x0]))
            print('')
            numerator_value = table[col_index][f1] - table[col_index][f0]
            denominator_value = table[0][x1] - table[0][x0]
            fin.append(numerator_value/denominator_value)

        table.append(fin)
        print(table)


if __name__ == '__main__':
    setup_table()
    generate_div_table()
    #print(table)
    #print "Hello World!"
