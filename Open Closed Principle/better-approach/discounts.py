from schools.mit import MIT
from schools.harvard import Harvard
from schools.standford import Standford

class Discount:
    def __init__(self, base_deduction = None):
        self.schools = [
            MIT(),
            Harvard(),
            Standford()
        ]
        self.base_deduction = 20
        if base_deduction:
            self.base_deduction = base_deduction

    def calculate_discounted_fee(self, student):
        for school in self.schools:
            if school.is_match(student.get('school')):
                return school.calculate_discount(self.base_deduction)


discount = Discount()
student = {
    'school': 'Harvard University'
}
print(discount.calculate_discounted_fee(student))
