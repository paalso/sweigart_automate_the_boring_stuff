def max_column_width(table, colnum):
    return max(*[len(cell) for cell in table[colnum]])


def table_to_string(table):
    columns_widths = [max_column_width(table, col)
            for col in range(len(table))]

    lines = []
    for colnum in range(len(table[0])):
        cells_list = map(lambda cell, colwidth: cell.rjust(colwidth),
                [row[colnum] for row in table], columns_widths)
        lines.append(" ".join(cells_list))

    return "\n".join(lines)


def print_table(table):
    print(table_to_string(table))


table_data = [
    ['apples', 'cherries', 'oranges', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
