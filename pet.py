class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def bark(self):
    print(f"{self.name} says woof!")

  def play_fetch(self):
    print(f"{self.name} loves playing fetch!")

# Create an object (instance) of the Dog class
my_dog = Dog("Pumpkin", "Golden Retriever", 3)

# Access object attributes
print(f"Dog's name: {my_dog.name}")
print(f"Dog's breed: {my_dog.breed}")
print(f"Dog's age: {my_dog.age}")

# Call object methods
my_dog.bark()
my_dog.play_fetch()
