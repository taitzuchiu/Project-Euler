#Sort player hands
def player_hands(filename, player1, player2):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        cards = line.split(" ")

        player1hand = []
        player2hand = []

        for i in range(0, 10):
            card = cards[i]
            value = card[0]
            suit = card[1]

            if (i < 5):
                player1hand.append((value, suit))
            else:
                player2hand.append((value, suit))

        player1.append(player1hand)
        player2.append(player2hand)

def get_values(hand):
    values = []
    faces = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for card in hand:
        value = card[0]
        if value.isdigit():
            values.append(int(value))
        else:
            values.append(int(faces[value]))

    values.sort()
    return values

def get_unique_vals(values):
    unique_vals = []
    for val in values:
        if val not in unique_vals:
            unique_vals.append(val)
    return unique_vals

def get_suits(hand):
    suits = []
    for card in hand:
        if card[1] not in suits:
            suits.append(card[1])
    return suits

#ROYAL FLUSH: T, J, Q, K, A in same suit
def royal_flush(values, suits):
    #Check if royal first
    royals = ['T', 'J', 'Q', 'K', 'A']

    for val in values:
        if (val in royals):
            royals.remove(card[0])
        else:
            return False

    #Did not return false, therefore it IS royal
    #Now just check if it's a flush
    return (len(suits)==1)

#STRAIGHT FLUSH: All cards consecutive values of same suit
def straight_flush(values, suits):
    return (straight(values, suits) and (len(suits)==1))

#FOUR OF A KIND: 4 cards all of the same value.
def four_of_a_kind(values, suits):
    if ((values[0] == values[3]) or (values[1] == values[4])):
        return True
    else:
        return False

#FULL HOUSE: Three of a kind, and a pair
def full_house(values, suits):
    unique_vals = get_unique_vals(values)
    return (len(unique_vals)==2)

#FLUSH: ALl cards of the same suit
def flush(values, suits):
    return (len(suits)==1)

#STRAIGHT: All cards are consecutive values
def straight(values, suits):
    for i in range(0,4):
        if (int(values[i+1]) - int(values[i]) != 1):
            return False
    return True

#THREE OF A KIND: 3 cards of the same value
def three_of_a_kind(values, suits):
    return ((values[0] == values[1] and values[1] == values[2])
            or (values[1] == values[2] and values[2] == values[3])
            or (values[2] == values[3] and values[3] == values[4]))

#TWO PAIRS: 2 different PAIRS
def two_pairs(values, suits):
    unique_vals = get_unique_vals(values)
    return (len(unique_vals)==3)

#ONE PAIR: 2 cards of same value
def one_pair(values, suits):
    unique_vals = get_unique_vals(values)
    return (len(unique_vals)==4)
#compare card: Returns player with the highest value card
def compare_card(val1, val2):
    if (val1 > val2):
        return 1
    else:
        return 2

def high_card(values1, values2):
    uniq1 = get_unique_vals(values1)
    uniq2 = get_unique_vals(values2)

    i = len(uniq1) - 1
    j = len(uniq2) - 1
    while i >= 0 and j >= 0:
        if uniq1[i] > uniq2[j]:
            return 1
        elif uniq1[i] < uniq2[j]:
            return 2
        else:
            i = i - 1
            j = j - 1

def get_scores(values, suits):
    if royal_flush(values, suits):
        return 10
    elif straight_flush(values, suits):
        return 9
    elif four_of_a_kind(values, suits):
        return 8
    elif full_house(values, suits):
        return 7
    elif flush(values, suits):
        return 6
    elif straight(values, suits):
        return 5
    elif three_of_a_kind(values, suits):
        return 4
    elif two_pairs(values, suits):
        return 3
    elif one_pair(values, suits):
        return 2
    else:
        return 0

def tied_full_house(values1, values2):
    three1 = 0
    three2 = 0
    pair1 = 0
    pair2 = 0

    if (values1.count(values1[0]) == 3):
        three1 = values1[0]
        pair1 = values1[4]
    else:
        three1 = values1[4]
        pair1 = values1[0]

    if (values2.count(values2[0])==3):
        three2 = values2[0]
        pair2 = values2[4]
    else:
        three2 = values2[4]
        pair2 = values2[0]

    if three1 > three2:
        return 1
    elif three2 > three1:
        return 2
    else:
        if pair1 > pair2:
            return 1
        else:
            return 2

def tied_two_pairs(values1, values2):
    highest = high_card(values1, values2)
    uniq1 = get_unique_vals(values1)
    uniq2 = get_unique_vals(values2)

    for val in uniq1:
        values1.remove(val)
    for val in uniq2:
        values2.remove(val)

    if values1[1] > values2[1]:
        return 1
    elif values1[1] < values2[1]:
        return 2
    else:
        if values1[0] > values2[0]:
            return 1
        elif values1[0] < values2[0]:
            return 2
        else:
            return highest

def tied_one_pair(values1, values2):
    highest = high_card(values1, values2)
    uniq1 = get_unique_vals(values1)
    uniq2 = get_unique_vals(values2)

    for val in uniq1:
        values1.remove(val)
    for val in uniq2:
        values2.remove(val)

    if values1[0] > values2[0]:
        return 1
    elif values1[0] < values2[0]:
        return 2
    else:
        return highest

def tied_scores(score, values1, values2):
    if (score == 9): #straight flush
        return compare_card(values1[4], values2[4])
    if (score == 8): #four of a kind
        return compare_card(values1[2], values2[2])
    if (score == 7): #full house
        return full_house(values1, values2)
    if (score == 6): #flush
        return compare_card(values1[4], values2[4])
    if (score == 5): #straight
        return compare_card(values1[4], values2[4])
    if (score == 4): #three of a kind
        return compare_card(values1[2], values2[2])
    if (score == 3): #two pairs
        return tied_two_pairs(values1, values2)
    if (score == 2): #two pairs
        return tied_one_pair(values1, values2)
    if (score == 0):
        return compare_card(values1[4], values2[4])

#The main thing
def main():
    player1 = []
    player2 = []

    wins1 = 0
    wins2 = 0

    player_hands("poker.txt", player1, player2)

    for i in range(0,1000):
        values1 = get_values(player1[i])
        values2 = get_values(player2[i])
        suits1 = get_suits(player1[i])
        suits2 = get_suits(player2[i])

        score1 = get_scores(values1, suits1)
        score2 = get_scores(values2, suits2)

        if score1 > score2:
            wins1 += 1
        elif score1 < score2:
            wins2 += 1
        else:
            if tied_scores(score1, values1, values2) == 1:
                wins1 += 1
            else:
                wins2 += 1
        """
        if score1 == 5 or score2 == 5:
            print(i+1, ":", score1, score2, wins1, wins2)"""

        #print ("wins: ", wins1," ", wins2)

    print (wins1)
    print (wins2)

    #print (player1)
    #print (get_values(player2[2]))

    #do thing

main()
