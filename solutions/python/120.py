class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")

Dog.bark = lambda self: "Woof"