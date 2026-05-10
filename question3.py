Student_list = []

class student:
    
    def __init__(self, student_id, name, department):
        
        self.student_id = student_id
        self.name = name
        self.department = department
        
        self.add_student()
    def add_student(self):
        Student_list.append(self)

        
student1 = student(201,"rakib","CSE")
student2 = student(202,"siyam","CSE")
