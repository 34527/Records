class GBAthlete:
    def __init__(self):
        self.name = '-'
        self.event = '-'
        self.medal = None

#main program
#create relay team
relay_team = []
#add athletes to relay team
for index in range(4):
    athlete = GBAthlete()
    athlete.name = input('Name of athlete: ')
    athlete.event = '4 x 100m (men)'
    relay_team.append(athlete)
#print relay team members and event
for index in range(len(relay_team)):
    print('{0} is in the {1}'.format(relay_team[index].name, relay_team[index].event))
