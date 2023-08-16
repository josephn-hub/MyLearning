def isValid():
    provideInput = input(' Enter whether the used is valid either True or False \n ')
    if provideInput == 'True':
        return True
    else:
        return False


calling = isValid()
print(calling)


class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def __str__(self):
        return f"Student name is {self.name} and age is {self.age} with the branch {self.branch}"

    # def __repr__(self):
    #     return f"Student name is {self.name} and age is {self} with the branch {self.branch}"

    def __add__(self, other):
        return Student(self.name + other.name, self.age + other.age, self.branch + other.branch)


student_1 = Student('joseph', '35', 'CSE')
student_2 = Student('Naveen', '30', 'ECE')

student_3 = student_1 + student_2
print(student_1)

print(student_3)
