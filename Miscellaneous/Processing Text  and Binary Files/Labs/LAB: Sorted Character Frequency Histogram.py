""" Estimated time
15-30 minutes

Level of difficulty
Medium

Prerequisites
4.3.1.15

Objectives
improve the student's skills in operating with files (reading/writing)
using lambdas to change the sort order.
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist'
(it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt

the expected output should look as follows:

a -> 3
b -> 2
c -> 1
output

Tip: Use a lambda to change the sort order."""

from os import strerror

file_name = input("Enter the file's name: ")
ch_count = {}
try:
    file = open(file_name, 'rt')
    ch = file.read(1).lower()
    while ch != '':
        if ch in ch_count.keys():
            ch_count[ch] += 1
        else:
            ch_count[ch] = 1
        ch = file.read(1).lower()
    file.close()

    file = open(file_name + '.hist', 'wt')
    for char in sorted(ch_count.keys(), key=lambda x: ch_count[x], reverse=True):
        file.write(char + ' -> ' + str(ch_count[char]) + '\n')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
