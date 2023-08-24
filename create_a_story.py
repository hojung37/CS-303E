print('You got lost as you were walking in the forest. As you try to find your way back home, you come across 2 different paths')
path = input('which path would you choose? [choose: narrow, wide] ')
if(path == 'narrow'):
    print('you arrive at a small cave','at the entrance there is a sign that says DANGER',sep='\n')
    move = input('what will you do?, [choose: go in, go back] ')
    if(move == 'go in'):
        print('as you go in, you find something shiny')
        shiny = input('it is a flashlight. will you grab it? [choose: yes, no] ')
        if(shiny == 'yes'):
            print('you were able to scare away the bats using the flashlight and find the door they were blocking')
            print('you go towards the door and open it. there is a map and a pearl inside it.')
            door = input('what would you grab? [choose: map, pearl] ')
            if(door == map):
                print('it is a map that shows the way to your house. you can find your way home now.','Congratulations!',sep='\n')
            elif(door == pearl):
                print('you find out that it was a pearl that attracts bees in the cave. you get attacked by bees.','you die',sep='\n')
            elif(shiny == 'no'):
                print('you got attacked by the bats in the dark.','you died',sep='\n')
    elif(move == 'go back'):
        print('a bear that was following you attacked you.','you died',sep='\n')
elif(path == 'wide'):
    print('you arrive at a castle','there is a huge gate infront of the castle but it\'s locked')
    gate = input('how will you open the door?,[choose: kick it, climb over it] ')
    if(gate == 'kick it'):
        print('BOOM!')
        print('because you made a big sound','you woke the monster that was gaurding the gate woke up')
        boom = input('it is coming towards you. what will you do?, [choose: run, fight] ')
        if(boom == 'run'):
            print('you found a small hole and was able to hide from the monster')
            staircase = input('in there you found a staircase. would you go up or down?, [choose: up, down] ')
            if(staircase == 'up'):
                print('you find a key by the end of the stairs')
                key = input('will you grab the key?, [choose: yes, no] ')
                if(key == 'yes'):
                    print('you were able to open the door at the end of the stairs. it is a door to your house', 'Congratulations!',sep='\n')
                elif(key == 'no'):
                    print('as you did not grab the key, you could not open the door at the end of the stairs.','you die',sep='\n')
            elif(staircase == 'down'):
                print('there was another monster downstairs','you died',sep='\n')
        elif(boom == 'fight'):
            print('you were too weak compared to the monster','you died',sep='\n')

    elif(gate == 'climb over it'):
        print('after you climb over, you see a monster that is sleeping')
        
                
else:
    print('you did not choose a path, you are trapped')

   
