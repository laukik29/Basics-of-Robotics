from student_class import student

student1 = student("jim", "Business", 3.1, False)
student2 = student("Pam", "Art", 2.5, True)

student3 = student("Oscar", "Accounting", 3.1, True)
student4 = student("Phyllis", "Engineering", 3.8 , True)

print(student3.on_honor_roll())
print(student4.on_honor_roll())
print(student1.name)
print(student2.gpa)
