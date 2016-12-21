####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import prisoners_dilemma
import globe
team_name = 'Artificial' # Only 10 chars displayed.
strategy_name = 'All I do is Win'
strategy_description = 'If I Fits I Sits'
num = 0
win = 1
def move(my_history, their_history, my_score, their_score):
    global num
    #print('Player 1: '+globe.pn[0]) #Prints player 1
    #print('Player 2: '+globe.pn[1]) #Prints player 2
    num += 1
    #Checks which player is the opponent
    if globe.pn[0] == 'team0':
        opponent = globe.pn[1]
    else:
        opponent = globe.pn[0]
    print('Opponents Move: '+str(globe.omoves))
    return 'b'       