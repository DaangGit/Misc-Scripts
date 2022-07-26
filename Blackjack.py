"""
Text based Blackjack game
Vedaang Raparthi
2021/07/04
"""
from random import choice

def dealcard(cards, person):
    '''
    Deals a card to a person's list from a list of cards.
    '''
    c = choice(cards)
    cards.remove(c)
    person.append(c)
    
    return None

def countvalue(h):
    '''
    Counts the value of the given hand 'h'
    '''
    
    tot = 0
    high_aces = 0
    #Calculating value
    for i in h:
        if i[0] == '1' and i[1] == '0':
            tot += 10
        elif i[0] in ['J','Q','K']:
            tot += 10
        elif i[0] == 'A':
            tot += 11
            high_aces += 1  
        else:
            tot += int(i[0])
    #checking for high aces
    while (tot > 21) and (high_aces >= 1):
        tot -= 10
        high_aces -= 1
    
    return tot

def shouldhit():
    '''
    Asks player to hit or stand
    '''
    choice = input('Hit or Stand? [h/s] '.rjust(69))
    print()
    return True if choice == 'h' else False

def drawaline():
    print()
    print(''.center(118,'-'))
    print()
    return None

def play(pwins, dwins):
    '''
    Takes player wins and dealer wins as arguments
    Plays a game
    Returns updated player wins and dealer wins
    '''
    #start seperator
    drawaline()

    #Initialising a list of all cards
    cards = [
        j + ' of ' + i 
        for i in ['Diamonds','Hearts','Clubs','Spades'] 
        for j in ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        ]

    #Lists for player and dealer cards
    dealer_cards = []
    player_cards = []
    
    #First three cards being dealt
    dealcard(cards, dealer_cards)
    dealcard(cards, player_cards)
    dealcard(cards, player_cards)

    #Beginning
    print(f'The dealer has {dealer_cards}'.center(118))
    print(f'Value: {countvalue(dealer_cards)}'.center(118), end = '\n\n')
    print(f'You have {player_cards}'.center(118))
    print(f'Value: {countvalue(player_cards)}'.center(118), end = '\n\n')
    
    #Player choosing to hit or stand
    while countvalue(player_cards) < 21 and shouldhit():
        dealcard(cards, player_cards)
        print(f'You now have {player_cards}'.center(118))
        print(f'Value: {countvalue(player_cards)}'.center(118), end = '\n\n')    
    
    #Checking value
    if countvalue(player_cards) > 21:
        print('You lost.'.center(118))
        dwins += 1
    
    elif countvalue(player_cards) == 21:
        print(' Blackjack! '.center(118,'$'), end = '\n\n')
        
        #Dealer drawing cards
        while countvalue(dealer_cards) < 18:
            dealcard(cards, dealer_cards)
            print('Dealer draws another card...'.center(118), end = '\n\n')
            print(f'The dealer now has {dealer_cards}'.center(118))
            print(f'Value: {countvalue(dealer_cards)}'.center(118), end = '\n\n')
        if countvalue(dealer_cards) == 21:
            print('You lost.'.center(118))
            dwins += 1
        else:
            print('You win.'.center(118))
            pwins += 1
    
    else:
        #Dealer drawing cards
        while countvalue(dealer_cards) < 18:
            dealcard(cards, dealer_cards)
            print('Dealer draws another card...'.center(118), end = '\n\n')
            print(f'The dealer now has {dealer_cards}'.center(118))
            print(f'Value: {countvalue(dealer_cards)}'.center(118), end = '\n\n')
        if countvalue(dealer_cards) <= 21 and (countvalue(dealer_cards) >= countvalue(player_cards)):
            print('You lost.'.center(118))
            dwins += 1
        else:
            print('You win.'.center(118))
            pwins += 1
    
    #end seperator
    drawaline()

    return pwins,dwins
    

    
#Game Title
print(''.center(118,'$'))
print(' BLACKJACK '.center(118,'$'))
print(''.center(118,'$'), end='\n\n')

#Wins and losses
pwins = 0
dwins = 0

#Start playing?
shallplay = input(' Play? [y/n] '.rjust(66))

while shallplay == 'y':
    pwins,dwins = play(pwins,dwins)
    
    shallplay = input(' Play one more time? [y/n] '.rjust(73))

print()

if shallplay == 'n':
    print(f'Player wins: {pwins}'.center(118))
    print(f'Dealer wins: {dwins}'.center(118))
    print(f'Win rate: {round((pwins / (pwins + dwins)) * 100, 2)}%'.center(118))
    print()
    print('Bye.'.center(118))