def enroll_student(self):
    if self.is_enrolled:
        print("student already enrolled")
    else:
        self.is_enrolled = True
    def drop_student(self):
        if not self.is_enrolled:
            print("Student is not enrolled")
        else:
            self.is_enrolled = False
