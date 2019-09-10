class Harvard:
    def is_match(self, school):
        return school.startswith("Harvard")
    
    def calculate_discount(self, base_deduction):
        return base_deduction * 1.8