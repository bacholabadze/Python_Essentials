""" Estimated time
30-90 minutes

Level of difficulty
Medium

Objectives
improve the student's skills in operating with files (reading)
perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.
Scenario
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file
contains three elements: the student's first name, the student's last name, and the number of point the
student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5
samplefile.txt

Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
Andrew Cox 	 1.5
Anna Boleyn 	 15.5
John Smith 	 7.0
output

Note:

your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness,
or any input data failures; encountering any data error should cause immediate program termination, and the
erroneous should be presented to the user;
implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should
be raised when a bad line is detect, and the third when the source file exists but is empty.
Tip: Use a dictionary to store the students' data."""


from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


student_data = {}

file_name = input("Enter students' data filename: ")

try:
    file = open(file_name, 'rt')
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        raise FileEmpty()

    for i in range(len(lines)):
        line = lines[i]
        columns = line.split()

        if len(columns) != 3:
            raise BadLine(i + 1, line)

        student = columns[0] + ' ' + columns[1]

        try:
            point = float(columns[2])
        except ValueError:
            raise BadLine(i + 1, line)

        try:
            student_data[student] += point
        except KeyError:
            student_data[student] = point

    for student in sorted(student_data.keys()):
        print(str(student) + '\t' + str(student_data[student]))

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except BadLine as e:
    print("Bad line #" + str(e.line_number) + " in source file: ", e.line_string)
except FileEmpty:
    print("Source file empty")

