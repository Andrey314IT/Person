class Person:
  height = 170
  name = "Name"
  is_sad = True
  def __init__(self, height, name):
    self.name = name
    self.height = height

class Cat:
  color = "Black"
  height = 40
  age = 1 
  name = "Choky"
  
  def play_w_human(self, human):
    human.is_sad = False
    
  def _init__(self, height, age, name, color):
    self.name = name
    self.height = height
    self.age = age
    self.color = color


me = Person("Andrey", 170)
cat = Cat("Choky")
print(me.is_sad)
cat.play_w_human(me)
print("грустный -",  me.is_sad)