class Students:
    def __init__(self):
        self.name = []
        self.school = []

    def create_student(self, name, school):
        self.name.append(name)
        self.school.append(school)

    def get_students(self):
        return {
            'name', self.name,
            'school', self.school
        }

