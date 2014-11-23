# Cary Anderson - CS 301 Project 2
# Finished: Saturday 22 Nov, 2014
# Raheja - Tues/Thurs @ 1500


from numpy import poly1d


table = []


def rreplace(s, old, new, occurrence):
    """ Utility function to replace the last occurrence of a character in a string """
    li = s.rsplit(old, occurrence)
    return new.join(li)


def setup_table():
    """ Set up the table that holds x/y values """
    the_file = open("input.txt", "r")
    for enum, line in enumerate(the_file):
        line = line.replace("\n", "")
        tony = line.split(" ")
        table.append([])

        for i, number in enumerate(tony):
            table[enum].append(float(number))


def generate_div_table():
    """ Modify the table using the divided difference method """

    iteration = 0  # Keep track of how many columns we"ve done
    # iterate over every column past the first two
    for i in xrange(len(table[0]) - 1):
        col_index = 1 + i
        iteration += 1
        fin = []
        for j in xrange(len(table[0]) - iteration):
            x0 = f0 = j
            x1 = x0 + iteration
            f1 = f0 + 1
            numerator_value = table[col_index][f1] - table[col_index][f0]
            denominator_value = table[0][x1] - table[0][x0]
            appr = numerator_value/denominator_value
            fin.append(float(str(appr)))

        table.append(fin)


def print_table(table):
    """ Print our sideways table properly """
    rows = "  f " + " f(x) "

    # Print the column headers
    for enum, i in enumerate(table):
        if enum < 2:
            continue
        arf = " f["
        for j in range(enum):
            arf += ","
        arf += "] "
        rows += arf
    print(rows)

    # Print the actual rows of the table
    for current_row, i in enumerate(table[0]):
        row = ""
        for current_col, j in enumerate(table):
            offset = len(table[0]) - len(table[current_col])
            if (current_row-offset) < 0:
                row += ""
                continue
            else:
                row += "" + str(round(table[current_col][current_row-offset], 3)) + "  "
        print(" " + row)


def print_polynomial(table):
    """ Print the un-simplified polynomial using our table """
    polynomial = "" + str(table[1][0])
    for i in range(2, len(table)):
        temp_x = ""
        for j in range(i-1):
            temp_x += "(x-" + str(table[0][j]) + ")"
        temp_x = (str(table[i][0]) + temp_x)
        polynomial += " + " + temp_x
    print(polynomial)


def print_simplified():
    """ Print the simplified polynomial """
    polynomial = poly1d([])
    for i in range(1, len(table)):
        temp_x = poly1d([table[i][0]])
        for j in range(i-1):
            temp_x *= poly1d([1, (-1*table[0][j])])
        polynomial += temp_x
    print(polynomial)


def print_lagrange_polynomial():
    """ Generate interpolating polynomial using the Lagrange method. """
    finished = ""
    for i in range(len(table[0])):
        for j in range(len(table[0])):
            if j == i:
                continue
            finished += "(x-" + str(table[0][j]) + ")"
        denominator = 1
        for k in range(len(table[0])):
            if k == i:
                continue
            denominator *= (table[0][i] - table[0][k])
        finished += "(" + str(table[1][i]/denominator) + ") + "
    finished = rreplace(finished, '+', ' ', 1)
    print(finished)


if __name__ == "__main__":
    print("Welcome!")
    setup_table()
    generate_div_table()

    print("\nHere is the table:")
    print_table(table)

    print("\nThe interpolating polynomial is: ")
    print_polynomial(table)

    print("\nThe simplified interpolating polynomial is:")
    print_simplified()

    print("\nThe Lagrange interpolating polynomial is: ")
    print_lagrange_polynomial()