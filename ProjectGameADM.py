# Administrator Games

games = {
    'Red Dead Redemption 2': 'Rockstar',
    'Batman Arkham City': 'Rocksteady',
    'Spider man': 'Insomanic Games'
}


def add_game(games, new_game, new_enterprise):
    if new_game not in games:
        games[new_game] = new_enterprise
        print('Game add sucessfully!')
        return games
    else:
        print('This game already in the list!')
        return games
    
def remove_game(games, name):
     if name in games:
        games.pop(name)
        print('Game removed sucessfully!')
        return games
     else:
          print('This game doesnt exist!')
          return games

def show_games(games):
     for name, enterprise in games.items():
          print(f'{name}: from enterprise {enterprise}')

def find_game(games, name):
     if name in games:
          print(f'{name} | enterprise: {games[name]}')
     else:
          print('Game not found!')





    
while True:

        choice = input('What is you wish to make? (Add / Remove / List / Find / Exit): ')


        if choice == 'Add':
            new_game = input('What is game name?: ')
            new_enterprise = input('What is a enterprise make that?: ')
            games = add_game(games, new_game, new_enterprise)


        elif choice == 'Remove':
             name = input('What is a game you want remove?: ')
             games = remove_game(games, name)

        elif choice == 'List':
             show_games(games)

        elif choice == 'Find':
             name = input('What game do you want find?: ')
             find_game(games, name)
        elif choice == 'Exit':
             print('Okay, have a good day!')
             break
        
        else: 
             print('Wrong command or doesnt exist!')
