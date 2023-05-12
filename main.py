from random import random 
#1 Create class named after the type of Pokemon you selected, which inherits from the Pokemon class and has the additional: instance attributes, basic_attack and prob (probability). 

class ICE:
#Define __init()__ and __str()__ to take the basic_attack and probability into account.
 def __init__(self, Hp):
    self.basic_attack = " "
    self.recieve = 0
    self.prob = 0 
  
   def attack(self, opponent):
  print("{} attempts {}".format(self.name, self.basic_attack))
  opponent.recieve(self.basic_attack, self.prob)
    
  def recieve(self, basic_attack, prob, attack_type):
    if random.randint(0, 1) <= prob:
      damage = self.damage(attack_type)
      self.Hp -= damage
      print("{} receives {} damage".format(self.name, damage))
    else:
      print("It missed!!")
    return self.Hp <= 0
  #Define attack() for your type
  basic_attack = 'freezeShock'
  prob = 0.3

  #. For your Pokemon type, multiply the damage by 2 when battling a Pokemon type it is strong against and divide damage by 2 when battling a Pokemon type it is weak against. 
  if random()<self.prob and type(other)
      other.shocked = True
      print()
      print(other.name, 'is shocked')
      print(self.prob * 2)
      
  if random()<self.prob and type(other)
      other.shocked = False
      print(other.name, 'is not shocked')
      print( self.prob / 2)
     

      return 1

  
  
