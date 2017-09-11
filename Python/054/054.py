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

#FLUSH: ALl cards of the same suit
def flush(values, suits):
    return (len(suits)==1)

#STRAIGHT: All cards are consecutive values
def straight(values, suits):
    for i in range(0,4):
        if (int(values[i+1]) - int(values[i]) > 1):
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

#The main thing
def main():
    player1 = []
    player2 = []

    player_hands("poker.txt", player1, player2)

    #print (player1)
    print (get_values(player2[2]))

    #do thing

main()
