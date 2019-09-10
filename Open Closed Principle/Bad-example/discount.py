class Discount:
    def __init__(self):
        self.base_deduction = 5

    def get_discount(self, student):
        discount = 0
        if (student.startswith("STANDFORD")):
            discount = self.base_deduction * 1.4
        elif student.startswith("HARVARD"):
            discount = self.base_deduction * 1.8
        elif student.startswith("MIT"):
            discount = self.base_deduction
        # more discount
        return discount