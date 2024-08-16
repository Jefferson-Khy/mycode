#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    How to win:
        Get to the Garden with a key and a potion
        Avoid the monsters!
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []
totalPlayerMoves = 0
poisonCounter = 0
pickedUpPoison = False
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Living Space',
                  'west'  : 'Pool',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Room1',
                  'item' : 'potion',
                  'description' : 'The dining table is fully set and every plate has food, but it seems noone is here. You may go East or West from here.'
               },
            'Room1' : {
                  'west' : 'Dining Room',
                  'east' : 'Bathroom',
                  'item' : 'plate',
                  'description' : 'This room is empty except for a bottle of Dr Pepper on the floor. You may go East or West from here.'
                },
            'Bathroom' : {
                'west'  : 'Room1',
                'item'  : 'pills',
                'description' : 'This sink and shower are left running, the lights dont work. You may go  West from here.'
                },
            'Garden' : {
                  'north' : 'Dining Room'
                },
            'Pool' : {
                'east' : 'Hall',
                'south': 'Basement',
                'item' : 'coin',
                'description' : 'The water is murky and you can not see to the bottom. You may go East or South  from here.'
                },
            'Basement' : {
                'north': 'Pool',
                'item' : 'skull',
                'description' : 'Its dark and cold in here, nothing interesting it seems. You may go North from here.'
                }
         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            totalPlayerMoves += 1
            if pickedUpPoison:
                if poisonCounter > 0:
                    poisonCounter -= 1
                    print("Find the potion", poisonCounter, "moves left.")
                elif poisonCounter == 0 and ('potion' in rooms['Dining Room'].values() or 'potion' in inventory):
                    print('The light is fading...Game Over!')
                    break
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    if move[0] == 'take':
        if move[1] in inventory and move[1] == "pills":
            print('You start to feel drowzy.....find the potion fast.')
            inventory.remove(move[1])
            poisonCounter = 2
            pickedUpPoison = True
            print('Find the potion', poisonCounter, 'moves left.')
        elif move[1] in inventory and move[1] == "potion":
            print('You feel better')
            inventory.remove(move[1])
            poisonCounter = 0
            pickedUpPoison = False
            print('That was close.')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

