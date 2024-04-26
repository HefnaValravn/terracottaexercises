class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def weight_in_kg(self):
        return self.__weight_in_kg
    
    @weight_in_kg.setter
    def weight_in_kg(self, value):
        self.__weight_in_kg = value
    
    @property
    def height_in_m(self):
        return self.__height_in_m
    
    @height_in_m.setter
    def height_in_m(self, value):
        self.__height_in_m = value

    @property
    def bmi(self):
        return self.__weight_in_kg / self.__height_in_m ** 2
    
    @property
    def category(self):
        calc = self.__weight_in_kg / self.__height_in_m ** 2
        if calc < 18.5:
            return 'underweight'
        elif calc < 25:
            return 'normal'
        else:
            return 'overweight'