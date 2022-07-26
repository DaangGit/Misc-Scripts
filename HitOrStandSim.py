"""
Hit or stand strategy tester
Vedaang Raparthi
2021/07/05
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

def countvalue(hand):
    '''
    Counts the value of the given hand
    '''

    tot = 0
    high_aces = 0
    
    #Calculating value
    for i in hand:
        if (i[0] == '1' and i[1] == '0') or i[0] in ['J','Q','K']:
            tot += 10
        elif i[0] == 'A':
            tot += 11
            high_aces += 1  
        else:
            tot += int(i[0])
    
    #Checking for high aces
    while (tot > 21) and (high_aces >= 1):
        tot -= 10
        high_aces -= 1
    
    return tot


def player_shouldhit(player_cards):
    '''
    Player's Strategy:
    Choose whether to hit or stand based on certain parameters.
    '''
    while countvalue(player_cards) < 18:
        return True
    else:
        return False

def dealer_shouldhit(dealer_cards):
    '''
    Dealer's Strategy:
    Choose whether to hit or stand based on certain parameters.
    '''
    while countvalue(dealer_cards) < 18:
        return True
    else:
        return False

player_wins = 0
dealer_wins = 0

def simulate_game():
    '''
    Simulates a game and returns results in the form of [ player wins, dealer wins ]
    '''
    result = [0,0]

    cards = [
        j + i 
        for i in ['D','H','C','S'] 
        for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        ]
    
    player_cards = []
    dealer_cards = []
    
    dealcard(cards, dealer_cards)
    dealcard(cards, player_cards)
    dealcard(cards, player_cards)
    
    while player_shouldhit(player_cards):
        dealcard(cards, player_cards)
    
    while dealer_shouldhit(dealer_cards):
        dealcard(cards, dealer_cards)
    
    if (
        (countvalue(player_cards) <= 21 and countvalue(dealer_cards) <= 21 
        and countvalue(player_cards) > countvalue(dealer_cards)) 
        
        or 
        
        (countvalue(player_cards) <= 21 and countvalue(dealer_cards) > 21)):
        #Player win        
        result[0] = 1
        result[1] = 0
    
    else:
        #Dealer win
        result[0] = 0
        result[1] = 1
    
    return result


n = int(input("Number of simulations: "))
for i in range(n):
    k = simulate_game()
    player_wins += k[0]
    dealer_wins += k[1]

print(f'Player wins: {player_wins}')
print(f'Dealer wins: {dealer_wins}')
print(f'Win rate: {round((player_wins / (player_wins + dealer_wins)) * 100, 2)}%')

end = input("Press enter to terminate.")