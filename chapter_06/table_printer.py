def print_table(table):
    col_widths = [0] * len(table)

    # retrieve max column widths for each nested list
    for y in range(len(table)):
        for x in table[y]:
            if col_widths[y] < len(x):
                col_widths[y] = len(x)

    # "rotate" and print the values of the nested lists
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(col_widths[y]), end=' ')
        print()
        x += 1


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)
