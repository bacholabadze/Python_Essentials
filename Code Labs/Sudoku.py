my_table = """
123456789
234567891
345678912
456789123
567891233
678912345
789123456
891234567
912345678
"""


def validSudoku(table):
    table = table.strip().split("\n")
    # print(table)

    if checkHorizontal(table) and checkVertical(table) and check3x3(table):
        print("Valid Sudoku")
    else:
        print("Not Valid Sudoku")


def numCountCheck(row):
    """ Checks if row contains numbers 1-9 without repeating"""
    for i in range(1, 10):  # which num to count.
        if not row.count(str(i)) == 1:  # if number count is different from one (e.g num is used twice or more times,
            return False  # or if it's not included at all, function will return false)
    return True  # otherwise return true


def checkHorizontal(table):
    """ Checks Sudoku Horizontally →"""
    for ix in range(9):  # row index
        if not numCountCheck(table[ix]):  # If function returns False
            print('[!] Failed in Horizontal Testing')
            return False
    print('[+] Successfully Finished Horizontal Testing')
    return True


def checkVertical(table):
    """ Checks Sudoku Vertically  ↓"""
    for ri in range(9):  # row index
        current_column = ''
        for ci in range(9):  # column index
            current_column += table[ci][ri]
        if not numCountCheck(current_column):  # call function numCountCheck on selected column
            print('[!] Failed in Vertical Testing')
            return False
    print('[+] Successfully Finished Vertical Testing')
    return True


def check3x3(table):
    # x, y = 0, 0               # coordinates as row and column
    end_x, end_y = 3, 3
    while end_x != 12 and end_y != 12:  # while selecting is not finished fully
        tmp = ""
        for x in range(end_x - 3, end_x):
            for y in range(end_y - 3, end_y):
                # print(x, y)
                tmp += table[x][y]
        if not numCountCheck(tmp):
            print("[!] Failed in 3x3 Testing")
            return False

        # print("-" * 10, tmp)
        end_y += 3
        if end_y > 9:
            # print("Gadacdaa")
            end_y = 3
            end_x += 3
    else:
        print("[+] Successfully Finished 3x3 Testing", end_y, end_x)
        return True


validSudoku(my_table)
