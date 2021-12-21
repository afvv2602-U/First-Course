print('Welcome to the Basketball Roster Program\n')
teamRoster = []
positions = ['Point Guard:','Shooting Guard:','Small Forward:','Power Forward:','Center:']
 
'''Inputs from user'''
teamRoster.append(str(input('Who is your point guard: ')).capitalize())
teamRoster.append(str(input('Who is your shooting guard: ')).capitalize())
teamRoster.append(str(input('Who is your small forward: ')).capitalize())
teamRoster.append(str(input('Who is your power forward: ')).capitalize())
teamRoster.append((input('Who is your center: ')).capitalize())

print('\nYour starting 5 for the upcoming basketball season')
for i in range(len(teamRoster)):
    print(str(positions[i])+'\t'+str(teamRoster[i]))

'''Remove the small forward and replace it'''
added_player = str(input(('\nOh no, '+str(teamRoster[2])+' is injured \nYour roster only has 4 players \nWho will take '+str(teamRoster[2])+' spot: '))).capitalize()
teamRoster[2] = added_player

print('\nYour starting 5 for the upcoming basketball season')
for i in range(len(teamRoster)):
    print(str(positions[i])+'\t'+str(teamRoster[i]))
print('Good luck '+added_player+' you will do great! \nYour roster now has 5 players')