class Standford:
    def is_match(self, school):
        return school.startswith("Standford")
    
    def calculate_discount(self, base_deduction):
        return base_deduction * 1.2