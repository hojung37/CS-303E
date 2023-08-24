#hojung kim 4/18 hw8
import random

class Car:
  def __init__(self,s):
    self.name = s
    self.speed = random.randint(60,100)
    self.max_distance = random.randint(450,550)

  def __str__(self):
    return self.name + ' Speed: '+ str(self.speed) + ' Max Distance: '+ str(self.max_distance)

class Race:
  def __init__(self,distance): 
    self.distance = distance
  
  def startRace(self,racers):
    self.racer_list =  []
    for i in range(racers): 
      Car("Car {}".format(i))
      c = Car('Car'+str(i))
      self.racer_list.append(c) 
      print(c)
  
  def __str__(self):
    display = ''
    for c in self.racer_list:
      display += (str(c)+'')
    return display 
  
  def getWinner(self):
    winner = 'No winner'
    for i in self.racer_list: 
        if (i.max_distance >= self.distance):
            if(winner == 'No winner'):
                winner = i
            elif (i.speed > winner.speed):
                winner = i 

    return 'winner:' + winner.name
    

def main():
    indy = Race(500)
    indy.startRace(18)
    print(indy.getWinner())
    
if __name__=="__main__":
    main()

