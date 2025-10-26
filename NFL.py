class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f'{self.playerName} ({self.playerPosition})'

class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def display_team(self):
        print(f'Team: {self.teamName}')
        print('Players:')
        for player in self.players:
            print(f'  {player}')

playerList = [
    Player('Sam Darnold', 'QB'),
    Player('Jaxon Smith-Njigba', 'WR'),
    Player('Kenneth Walker', 'RB'),
    Player('Jason Myers', 'K')
]

team = NFLTeam('Seattle Seahawks', playerList)
team.display_team()
