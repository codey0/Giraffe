class Student:
    # class is an overview of what the "Student" datatype is
    # object is an actual "Student"
    # below is an initialize function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        # above means that the name of the Student object is going to be equal to the name that we passed
        # similar logic for below statements
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False