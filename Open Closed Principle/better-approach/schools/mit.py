class MIT:
    def is_match(self, school):
        return school.startswith("MIT")
    
    def calculate_discount(self, base_deduction):
        return base_deduction * 1.4