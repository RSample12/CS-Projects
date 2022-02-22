#  File: Poker.py

#  Description:

#  Student's Name: Riley Sample

#  Student's UT EID: rcs3396

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created:2/14/22

#  Date Last Modified:

import sys, random


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []  # All of players hands in 2-D list
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())  # Creates list for player then appends their hand to players_hands
            self.players_hands.append(hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        print()
        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        # find out which hand they have
        hand_points = []  # create a list to store points for hand
        points = 0
        type = ''
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand

        # Determines type of hand a player has
        for hand in self.players_hands:
            points, type = self.is_royal(hand)
            if points != 0:
                hand_type.append(type)
                hand_points.append(points)
            else:
                points, type = self.is_straight_flush(hand)
                if points != 0:
                    hand_type.append(type)
                    hand_points.append(points)
                else:
                    points, type = self.is_four_kind(hand)
                    if points != 0:
                        hand_type.append(type)
                        hand_points.append(points)
                    else:
                        points, type = self.is_full_house(hand)
                        if points != 0:
                            hand_type.append(type)
                            hand_points.append(points)
                        else:
                            points, type = self.is_flush(hand)
                            if points != 0:
                                hand_type.append(type)
                                hand_points.append(points)
                            else:
                                points, type = self.is_straight(hand)
                                if points != 0:
                                    hand_type.append(type)
                                    hand_points.append(points)
                                else:
                                    points, type = self.is_three_kind(hand)
                                    if points != 0:
                                        hand_type.append(type)
                                        hand_points.append(points)
                                    else:
                                        points, type = self.is_two_pair(hand)
                                        if points != 0:
                                            hand_type.append(type)
                                            hand_points.append(points)
                                        else:
                                            points, type = self.is_one_pair(hand)
                                            if points != 0:
                                                hand_type.append(type)
                                                hand_points.append(points)
                                            else:
                                                points, type = self.is_high_card(hand)
                                                hand_type.append(type)
                                                hand_points.append(points)

        for i in range(len(hand_type)):
            print('Player ' + str(i + 1) + ': ' + hand_type[i])

        # test for tie
        tied_test = {"Royal Flush": 0, "Straight Flush": 0, "Four of a Kind": 0, "Full House": 0,
                     "Flush": 0, "Straight": 0, "Three of a Kind": 0, "Two Pair": 0, "One Pair": 0, "High Card": 0}

        for hand in hand_type:
            tied_test[hand] += 1

        # If the number of winning hands is > 1, then there is a tie
        hand_type_tied = ''
        tie = False
        for i in tied_test:
            if tied_test[i] == 1:
                break
            if tied_test[i] > 1:
                tie = True
                hand_type_tied = i
                break

        # determine winner and print
        winner_index = 0
        for i in range(len(hand_points)):
            if hand_points[i] > hand_points[winner_index]:
                winner_index = i

        print()
        # If it is tie, prints player in order of most points
        # else print winner
        if tie:
            tied_points = []
            for i in range(len(hand_points)):
                if hand_type[i] == hand_type_tied:
                    tied_points.append(hand_points[i])
            tied_points.sort(reverse=True)

            for points in tied_points:
                print("Player", hand_points.index(points) + 1, "ties.")

        else:
            print("Player", winner_index + 1, "wins.")

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if not same_suit:
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if not rank_order:
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    # A straight flush is made of 5 cards in numerical sequence but of the same suit.
    def is_straight_flush(self, hand):
        # checks if hand is same suit
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if not same_suit:
            return 0, ''

        ranks = []
        for card in hand:
            ranks.append(card.rank)

        ranks.sort()
        for i in range(len(ranks) - 1):
            if ranks[i] != ranks[i + 1] - 1:
                return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    # In four of a kind, the hand must have four cards of the same numerical rank, e.g. four aces or four queens.
    def is_four_kind(self, hand):
        card_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in hand:
            card_dict[card.rank] += 1

        c123 = 0
        c4 = 0
        four_of_kind = False
        for i in card_dict:
            if card_dict[i] == 4:
                four_of_kind = True
                c123 = i
            if card_dict[i] == 1:
                c4 = i

        if four_of_kind:
            points = 8 * 15 ** 5 + c123 * 15 ** 4 + c123 * 15 ** 3
            points = points + c123 * 15 ** 2 + c123 * 15 ** 1
            points = points + c4
            return points, "Four of a Kind"
        else:
            return 0, ''

    # For a full house, three of the cards must have the same numerical rank and the the two remaining
    # cards must also have the same numerical rank but obviously different rank than the other three.
    def is_full_house(self, hand):
        card_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in hand:
            card_dict[card.rank] += 1

        c123 = 0
        c4 = 0
        for i in card_dict:
            if card_dict[i] == 3:
                c123 = i
            if card_dict[i] == 2:
                c4 = i

        if c123 != 0 and c4 != 0:
            points = 7 * 15 ** 5 + c123 * 15 ** 4 + c123 * 15 ** 3
            points = points + c123 * 15 ** 2 + c4 * 15 ** 1
            points = points + c4
            return points, "Full House"
        else:
            return 0, ''

    # In a flush there are 5 cards all of the same suit. The numerical order does not matter.
    def is_flush(self, hand):
        suit_dict = {'C': 0, 'D': 0, 'H': 0, 'S': 0}
        flush = False
        cntr = 0
        for card in hand:
            suit_dict[card.suit] += 1

        for i in suit_dict:
            if suit_dict[i] == 5:
                flush = True

        if flush:
            points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
            return points, 'Flush'
        else:
            return 0, ''

    def is_straight(self, hand):
        ranks = []
        for card in hand:
            ranks.append(card.rank)

        ranks.sort()
        for i in range(len(ranks) - 1):
            if ranks[i] != ranks[i + 1] - 1:
                return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_three_kind(self, hand):
        card_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in hand:
            card_dict[card.rank] += 1

        three_kind = False
        for i in card_dict:
            if card_dict[i] == 3:
                three_kind = True

        if three_kind:
            points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
            return points, "Three of a Kind"
        else:
            return 0, ''

    def is_two_pair(self, hand):
        card_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in hand:
            card_dict[card.rank] += 1

        c12 = 0
        c34 = 0
        c5 = 0
        for i in card_dict:
            if card_dict[i] == 2:
                if i > c12:
                    c12, c34 = i, c12
                if c12 == 0:
                    c12 = i
            if card_dict[i] == 1:
                c5 = i

        if c12 != 0 and c34 != 0 and c5 != 0:
            points = 3 * 15 ** 5 + c12 * 15 ** 4 + c12 * 15 ** 3
            points = points + c34 * 15 ** 2 + c34 * 15 ** 1
            points = points + c5
            return points, "Two Pair"
        else:
            return 0, ''

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):
        card_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in hand:
            card_dict[card.rank] += 1

        c12 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        for i in card_dict:
            if card_dict[i] == 2:
                c12 = i
            if card_dict[i] == 1:
                if i > c4:
                    c4, c5 = i, c4
                if i > c3:
                    c3, c4 = i, c3
                if c3 == 0:
                    c3 = i

        if c12 != 0 and c3 != 0 and c4 != 0 and c5 != 0:
            points = 2 * 15 ** 5 + c12 * 15 ** 4 + c12 * 15 ** 3
            points = points + c3 * 15 ** 2 + c4 * 15 ** 1
            points = points + c5
            return points, "One Pair"
        else:
            return 0, ''

    def is_high_card(self, hand):

        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, "High Card"


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()


if __name__ == "__main__":
    main()
