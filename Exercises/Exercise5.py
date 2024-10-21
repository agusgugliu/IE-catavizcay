'''
EXERCISE N°5
Write a program that stores the dictionary with the credits of the subjects of a course {'Mathematics': 6, 'Physics': 4, 'Chemistry': 5} and then displays the credits of each subject in the format <subject> has <credits> credits, where <subject> is each of the subjects of the course, and <credits> are its credits. At the end it should also show the total number of credits for the course.
'''

courses = {
    'Mathematics': 6, 
    'Physics': 4, 
    'Chemistry': 5}

total_credits = 0

for c in courses:
    print(f"{c} has {courses[c]} credits")
    total_credits += courses[c]

print(f"Total credits: {total_credits}")