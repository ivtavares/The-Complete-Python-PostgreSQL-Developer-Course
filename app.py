#Dictionaries in Python
#sample_set = {3, 5, 9, 1, 1}

#sample_dictionary = {3:7, 2: 25}
#print(sample_dictionary[3])
#sample_dictionary = {'name': 'Jose', 'mark': 70}
#print(sample_dictionary['name'])

#Advanced Dictionary usage in Python
# student = {'name': 'Jose',
#                      'marks': [70, 60, 100, 89, 83],
#            'exams': {
#                'final': 70,
#                'midterm': 50
#            }
#            }
# print(student['exams']['final'])

def create_student():
    """Ask the user for the student's name
    Create the dictionary
    Return the dicionary
    """
    student = {'name': input('Write the student name: '),
               'marks': []}
    return student

print(create_student())

