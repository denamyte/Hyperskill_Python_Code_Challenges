class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    def __str__(self):
        return f'Model: {self.model}; color: {self.color}'


tesla_car = Tesla('S3', 'black')
# print(tesla_car)
