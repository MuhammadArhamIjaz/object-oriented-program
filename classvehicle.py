class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
modelx=vehicle(240,18)
print(modelx.max_speed)
print(modelx.mileage)
print("model maximam speed is ",modelx.max_speed,"kmph")
print("model mileage is ",modelx.mileage,"kmph")
