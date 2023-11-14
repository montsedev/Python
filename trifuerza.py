#     *
#    ***
#   *****
#  *     *
# ***   ***
#***** *****

def print_triforce(rows: int):

    for row in range(0, rows * 2):
        start_space = ' ' * ( ( ( 2 * rows ) - 1) - row)
        print_row = '*' * ((2 * (row + 1)) -1)
        print(f"{start_space}{print_row}")
print_triforce(3)