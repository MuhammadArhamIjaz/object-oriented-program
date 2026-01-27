class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("DEstructor called")
def Createobj():
    print("Making object...")
    obj=Employee()
    print("Fumction ends")
    return obj
print("Calling Create_obj() function....") 
obj=Createobj()
print("Program ends")