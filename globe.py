pn = []
omoves = 'NaN'
run = 0
globe_change = 'false'
def globe_checkopp():
    global pn
    opp = 'NaN'
    #Checks which player is the opponent
    if pn[0] == 'team0':
        opponent = pn[1]
        opp = 'player2'
    else:
        opponent = pn[0]
        opp = 'player1'
    #print('Opponent: '+str(opponent))
    
    return str(opp)
def globe_run():
    global run
    global omoves
    global globe_change
    if run >= 4:
        run = 0
        globe_change = 'true'
        omoves = 'c'
    else:
        run += 1
        globe_change = 'false'
def omove(i):
    return