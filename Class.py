class Parrot:
    # instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # instance method
    def sing(self,song):
        return "{} sing {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing {}".format(self.name,self.age)
    
# instance the object
blu = Parrot("BLU",10)

# call our instance method
print(blu.sing("Happy"))
print(blu.dance())
