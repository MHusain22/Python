class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
# child class
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Pengu is ready")
    def whoisThis(self):
        print("Peng")
    def run(self):
        print("Run and run")
    
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()