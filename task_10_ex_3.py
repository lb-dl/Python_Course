"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, 'r') as f:
        f_reader = csv.DictReader(f)
        sortedlist = sorted(f_reader, key=lambda row: float(row['average mark']), reverse=True)
        top_students = []
        count = 0
        for dic in sortedlist:
            if count != number_of_top_students:
                top_students.append(dic['student name'])
                count += 1
        return top_students


def write_students_age_desc(file_path, output_file):
    with open(file_path, 'r') as f:
        f_reader = csv.DictReader(f)
        sortedlist = sorted(f_reader, key=lambda row: int(row['age']), reverse=True)
        print(sortedlist)

    with open(output_file, 'w') as f:
        fieldnames = ['student name', 'age', 'average mark']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)
