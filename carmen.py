'''
Author:          Shariq Moghees
File:            carmen.py
Date:            5/14/23
Description:     A program made to run a version of the game "Where in the World is
Carmen Sandiego?" by implementing recursive DFS algorithms into some functions.
'''

'''
Below is the game dictionary: A big dictionary with 4 sub-dicts within.
1. locations: a dict of locations with connecting locations, whether the location is locked, and whether carmen is there
2. people: a dict of people with their location, dialogue string, and what locations/people/clues they unlock
3. clues: a dict of every clue and its location, clue text, and what location/people/clues they unlock
4. current-location: intitally Rome and then will update via functions as the player travels
'''
game = {
"locations": {"Rome": {"connections": ["Paris", "London"], "starts-locked": False, "carmen": False}, "Paris": {"connections": ["London", "Marseilles", "Berl\
in"], "starts-locked": True, "carmen": False}, "Moscow": {"connections": ["Berlin"], "starts-locked": True, "carmen": True}, "Berlin": {"connections": ["Par\
is", "Marseilles", "Moscow"], "starts-locked": True, "carmen": False}, "London": {"connections": ["Paris", "Rome"], "starts-locked": True, "carmen": False},\
 "Marseilles": {"connections": ["Paris"], "starts-locked": True, "carmen": False}},
"people": {"James": {"location": "London", "conversation": "I hear she may have ran off to Berlin. Try searching the Brandenburg-Gate.", "starts-hidden": Fa\
lse, "unlock-locations": ["Berlin"], "unlock-people": [], "unlock-clues": ["Brandenburg-Gate"]}, "Henri": {"location": "Paris", "conversation": "An investig\
ator in London named James has a clue for you.  ", "starts-hidden": True, "unlock-locations": ["London"], "unlock-people": ["James"], "unlock-clues": []}, "\
Giuseppe": {"location": "Rome", "conversation": "Hi, your goal is to catch Carmen, you need to talk to Luca.  He's here in town.  ", "starts-hidden": False,\
 "unlock-locations": [], "unlock-people": ["Luca"], "unlock-clues": []}, "Luca": {"location": "Rome", "conversation": "Henri in Paris has lost his diamonds,\
 Carmen stole them! You should go and talk to him there.  ", "starts-hidden": True, "unlock-locations": ["Paris"], "unlock-people": ["Henri", "Nicolette"], \
"unlock-clues": []}, "Estelle": {"location": "Marseilles", "conversation": "She was here a while ago, I think she may have ran off back to Paris.  ", "start\
s-hidden": False, "unlock-locations": [], "unlock-people": [], "unlock-clues": []}, "Viktor": {"location": "Moscow", "conversation": "I saw her two days ago\
, you should search for her!", "starts-hidden": True, "unlock-locations": [], "unlock-people": [], "unlock-clues": []}, "Nicolette": {"location": "Paris", "\
conversation": "I hear that Estelle in Marseilles has some information for you.  ", "starts-hidden": True, "unlock-locations": ["Marseilles"], "unlock-peopl\
e": ["Estelle"], "unlock-clues": []}},
"clues": {"Brandenburg-Gate": {"location": "Berlin", "clue-text": "A note was left in cyrillic with the Moscow-Sheremetyevo airport.  ", "starts-hidden": Tr\
ue, "unlock-locations": ["Moscow"], "unlock-people": ["Viktor"], "unlock-clues": []}},
"current-location": "Rome"}

#Split this game dict into 3 stand-alone dicts to make things easier to navigate
#I didnt make a separate one for current-location because it is only one string.
game_locs = game['locations']
game_people = game['people']
game_clues = game['clues']

def can_go(locations, start, destination):
    '''
    :param locations: game_locs dict
    :param start: location u are in currently
    :param destination: location you want to travel
    :return: True or False

    The helper fucntion for can_go_rec that also keeps track of visited or
    "unlocked" places to trace an open path recursively to where we want to go
    '''

    visited = {}
    for place in locations:
        visited[place] = False

    #calls the recursive function
    return can_go_rec(locations, start, destination, visited)

def can_go_rec(locations, start, destination, visited):
    '''
    :param start: your starting location
    :param destination: the location you want to go to
    :param locations: game_locs dictionary
    :return: True or False

    This is the recursive function that will check if there is a path from you current location
    to where u want to go. Returns a boolean on whether there is an available path or not
    '''
    path = [] #stores the path as empty first and then add the path from our starting location to our destination
        visited[start] = True   #Sets our current location as unlocked
        #BASE CASE
        if start == destination:
            return True
        #RECURSIVE CASE
        for next_loc in locations[start]['connections']:
            if not visited[next_loc] and not locations[next_loc]['starts-locked']: #Checks to make sure the next loc is not visted and is unlocked
                if can_go_rec(locations, next_loc, destination, visited):
                    return True
    
        visited[start] = False
    
        #input validations
        if start == destination:
            print("you are currently at this location\n")
        else:
            print("You haven't unlocked this location yet\n")
        return False

def talk_to(locations, people, clues, person, spoken_list):
    '''
    :param locations: game_locs dict
    :param people: game_people dict
    :param clues: game_clues dict
    :param person: the name of the person we talk to
    :return: nothing

    This is the function which handles talking to people. Checks whether
    they're hidden, if they're at the location, and if they are in the people dictionary

    also unlocks all of the features of the game allowed by their conversation
    '''
     if person in people:

        #print dialogue
        print(people[person]['conversation'])
        people[person]['starts-hidden'] = False #unhides person

        #unlock associated locations
        for unlocked_loc in people[person]['unlock-locations']:
            locations[unlocked_loc]['starts-locked'] = False
        #unlock asscociated people
        for unlocked_person in people[person]['unlock-people']:
            people[unlocked_person]['starts-hidden'] = False
        #unlock associated clues
        for unlocked_clue in people[person]['unlock-clues']:
            clues[unlocked_clue]['starts-hidden'] = False

        if person not in spoken_list:
            spoken_list.append(person)

        else:  #input validation
            print('This person does not exist at this location (check spelling and capitlization)\n')

def investigate_clue(current_loc, locations, people, clues):
    '''
    :param current_loc: game['current-location']
    :param locations: locations dict
    :param people: people dict
    :param clues: clues dict
    :return: nothing

    Same as talk_to function but for investigating clues
    '''

    if current_loc in clues['Brandenburg-Gate']['location']:

        #print clue text
        print(clues['Brandenburg-Gate']['clue-text'])
        clues['Brandenburg-Gate']['starts-hidden'] = False #unhides clue

        #unlock associated locations
        for unlocked_loc in clues['Brandenburg-Gate']['unlock-locations']:
            locations[unlocked_loc]['starts-locked'] = False
        #unlock asscociated people
        for unlocked_person in clues['Brandenburg-Gate']['unlock-people']:
            people[unlocked_person]['starts-hidden'] = False
        #unlock associated clues
        for unlocked_clue in clues['Brandenburg-Gate']['unlock-clues']:
            clues[unlocked_clue]['starts-hidden'] = False

    else:  #input validation
        print('No such clue found at this location\n')

def is_carmen_here(current_loc, locations):
    '''
    :param current_loc: the current location the player is at
    :return: True or False
    '''
    if locations[current_loc]['carmen'] == True:
        return True
    return False

if __name__ == '__main__':
    found_carmen = False  #Win condition: You fin carmen after a successful search
    search_count = 0  #Lose: condition: You search 3 times without finding Carmen
    spoken_to = [] #A list to keep track of who we have spoken to already
    carmen_found = False
    game_over = False

    #game loop
    while not game_over:
        command = input('What would you like to do?: ')
        print('\n')
        #display commands

        if command == 'display people':
            for person in game_people:
                if game_people[person]['starts-hidden'] == False and game_people[person]['location'] == game['current-location']:
                    if person not in spoken_to:
                        print(f'{person}\tNot Spoken To Yet\n')
                    else:
                        print(f"{person}\t{game_people[person]['conversation']}\n")

        elif command == 'display locations':
            for loc in game_locs:
                if game_locs[loc]['starts-locked'] == False:
                    print(f'{loc}\n')

        elif command == 'display clues':
            for clue in game_clues:
                if game_clues[clue]['starts-hidden'] == False:
                    print(f'{clue}\n')

         #commands that implement other functions

        elif 'go to' in command or 'travel to' in command:
            if can_go(game_locs,game['current-location'], command.split(' ')[-1]):
                game['current-location'] = command.split(' ')[-1]
                print('You have travlled to ', game['current-location'],'\n')

        elif 'talk to' in command:
            talk_to(game_locs,game_people,game_clues,command.split(' ')[-1], spoken_to)

        elif 'investigate' in command:
            investigate_clue(game['current-location'], game_locs, game_people, game_clues)

        #catch carmen command. Directly realizes the win/lose conditions of the game

        elif command == 'catch carmen' or command == 'catch Carmen':
            carmen_found = is_carmen_here(game['current-location'], game_locs)
            if carmen_found: #If carmen is there
                game_over = True
                carmen_found = True
                search_count += 1
            elif not carmen_found and search_count >= 3: # If you have 3 unsucessful searches
                game_over = True
            else:
                search_count += 1
                print(f'Carmen is not here. You have used {search_count} of 3 searches\n')

        #quit/exit command
        elif command == 'quit' or command == 'exit':
            game_over = True
            print('You have exited the game\n')

        #input validations
        else:
            print("Not a valid command. Check spelling")

    #Endgame messages

    if carmen_found:
        print('You have caught Carmen Sandiego! You win the game!')
    else:
        print("You couldn't find Carmen Sandiego in 3 searches, You have lost the game!")
