table = []
print("Welcome!")


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
    iteration = 0  # Keep track of how many columns we've done
    # iterate over every column past the first two
    for i in xrange(len(table[0]) - 1):
        col_index = 1 + i
        iteration += 1
        fin = []
        for j in xrange(len(table[0]) - iteration):
            x0 = f0 = j
            x1 = x0 + iteration
            f1 = f0 + 1
            '''print('iteration = ' + str(iteration))
            print('x0: ' + str(x0) + ' x1: ' + str(x1))
            print('f0: ' + str(f0) + ' f1: ' + str(f1))
            print('col index = ' + str(col_index))
            print('Value f1 = ' + str(table[col_index-2][f1]))
            print('Value f0 = ' + str(table[col_index-2][f0]))
            print('Value x1 = ' + str(table[0][x1]))
            print('Value x0 = ' + str(table[0][x0]))
            print('')'''
            numerator_value = table[col_index][f1] - table[col_index][f0]
            denominator_value = table[0][x1] - table[0][x0]
            appr = numerator_value/denominator_value
            fin.append(float(str(appr)))

        table.append(fin)
        print(table)

# TODO: THIS
def generate_lagrange_table():
    """ Generate interpolating polynomial using the Lagrange method. """
    for i in table[0]:
        print i


def print_table():
    rows = ' f ' + ' f(x) '

    for enum, i in enumerate(table):
        if enum < 2:
            continue
        arf = ' f['
        for j in range(enum):
            arf += ','
        arf += '] '
        rows += arf
    print(rows)

    for count, i in enumerate(table[0]):
        print table[0][count]
        row = ' '
        for enum, j in enumerate(table):
            offset = len(table[0]) - len(table[enum]) -1
            if (count-offset) < 0:
                row += '    '
                continue
            else:
                row += str(i)
            print('count: ' + str(count))
            print('offset: ' + str(offset))
            print('difference: ' + str(count-offset))
            print('')
            #count - offset
            #print('offset: ' + str(offset))
            #row += ' ' + str(table[enum][count - offset]) + ' '
            #if offset > enum:
            #    continue
        print(' ' + row) #+ str(table[count][enum]))

    #for



if __name__ == '__main__':
    setup_table()
    generate_div_table()
    print('The interpolating polynomial is: ')
    polynomial = '' + str(table[1][0])

    for i in range(2, len(table)):
        temp_x = ''
        for j in range(i-1):
            temp_x += '(x-' + str(table[0][j]) + ')'
        temp_x = (str(table[i][0]) + temp_x)
        polynomial += ' + ' + temp_x
        print(polynomial)

    print("And here is the table:")
    print_table()
        #print(str(table[i][0]) + str(temp_x))
    #print(table)
    #print "Hello World!"
