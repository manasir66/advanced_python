#OOP class based on online tutorials 

#def a student class and relevent methods

class Student:

  def __init__(self, name, matric_no, age, grade):
    self.name = name
    self.matric_no = matric_no
    self.age = age
    self.grade = grade

  def get_name_matric(self):
    return self.name, self.matric_no
  
  def get_grade(self):
    return self.grade


class Course:

  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students 
    self.students = []  #empty list of students

  #create a method to add students to course that are part of the students class 

  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      print("Success")
      return True
    else:
      print("Unsuccessful") #if cannot add return false
      return False

  def get_avergae_grade(self):
    total = 0
    for student in self.students:
      total += student.get_grade()
    
    return round(total / len(self.students), 3)



s1 = Student("AA", 473, 23, 89)
s2 = Student("BB", 474, 19, 98)
s3 = Student("CC", 475, 21, 67)

student_list = [s1, s2, s3]

math = Course("Mathmematics", 3)

for i in student_list:
  math.add_student(i)

print(math.get_avergae_grade())