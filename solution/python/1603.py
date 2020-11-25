"""
@difficulty: easy
@tags: misc
@notes: intuitive
"""
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parkings = [-1, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parkings[carType] > 0:
            self.parkings[carType] -= 1
            return True
        else:
            return False
