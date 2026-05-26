import random
#import numpy as np
#import pandas as pd
#import mathplotlib
from abc import ABC, abstractmethod

class Player(ABC):
    """
    The docstring for each player will have two attributes separated by a
    slash. The first corresponds to the player's play style on defense, and
    the second corresponds to their play style on offence. More specifically:
    
    defense -> call / bluff frequency
        - Loose, Medium, Tight
    offence -> bet size
        - Weak, Medium, Agressive

    I understand that bluffing is offence, but it is more commonly associated
    with riskier play -- and fits with the attribute of calling

    Some players are called by the term commonly used by poker players,
    and some are named after the friends I play poker with who play
    with these styles (myself included).
    """

    def __init__(self, net_winnings=0, current_stack=50):

        self.net_winnings = net_winnings
        self.current_stack = current_stack
        self.hand = []
        self.five_card = []
        self.hand_type = "High Card"

    #def pot_odds(self):
    #    raise NotImplementedError

    #@abstractmethon
    #def am_i_good(self):
    #    raise NotImplementedError

class Card:

    def __init__(self, str_card_repr: str) -> None:
        """
        10 will be represented in the string as 0, but will have a value of 10
        2 - 9 -> actual value
        j -> 11
        q -> 12
        k -> 13
        a -> 15
        """
        self.val = 100
        self.suit = "undetermined"
        # determine value
        if True:
            if str_card_repr[0] == "0":
                self.val = 10
            elif str_card_repr[0] == "j":
                self.val = 11
            elif str_card_repr[0] == "q":
                self.val = 12
            elif str_card_repr[0] == "k":
                self.val = 13
            elif str_card_repr[0] == "a":
                self.val = 15
            else:
                self.val = int(str_card_repr[0])
        
        # determine suit
        if True:
            if str_card_repr[1] == "h":
                self.suit = "hearts"
            if str_card_repr[1] == "c":
                self.suit = "clubs"
            if str_card_repr[1] == "s":
                self.suit = "spades"
            if str_card_repr[1] == "d":
                self.suit = "diamonds"
        self.str_card_repr = str_card_repr

# class Fish(Player):
#     """
#     Loose / Weak
#     """

# class Wyatt(Player):
#     """
#     Loose / Medium
#     """
        
# class Lag(Player):
#     """
#     Loose / Agressive
#     """
        
# class Chedda(Player):
#     """
#     Medium / Weak
#     """

# class Dom(Player):
#     """
#     Medium / Medium
#     """

# class Kuhn(Player):
#     """
#     Medium / Agressive
#     """
    
# class Nit(Player):
#     """
#     Tight / Weak
#     """
    
# class Jaxon(Player):
#     """
#     Tight / Medium
#     """
    
# class Tag(Player):
#     """
#     Tight / Agressive
#    """


#Probably going in the loop
suits = ["h", "c", "s", "d"]
vals = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "0", "j", "q", "k"]
deck = []
for i in suits:
    for j in vals:
        strin = j + i
        deck.append(Card(strin))
straights = (
    "a2345", "23456", "34567", "45678", "56789",
    "67890", "7890j", "890jq", "90jqk", "0jqka"
            )

def my_hand(self):
    """
    Protocol: default to high card, check if each hand is possible,
    then if it is, assemble the best hand given the hand they have.
    """
    self.five_card = []
    val_collector = {"a": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                     "8": 0, "9": 0, "0": 0, "j": 0, "q": 0, "k": 0}
    
    suit_collector = {"h": 0, "c": 0, "s": 0, "d": 0}
    
    for card in self.hand:
        val_collector[card.str_card_repr[0]] += 1
        suit_collector[card.str_card_repr[1]] += 1

    suit_of_interest = "z"
    for key, item in suit_collector.items():
        if item > 4:
            suit_of_interest = key
            break

    high_card = True
    pair = False
    two_pair = False
    trips = False
    straight = False
    flush = False
    boat = False
    quads = False
    straight_flush = False
    royal = False

    # Check pair and two pair
    if max(val_collector.values()) == 2:
        count = 0
        for v in val_collector.values():
            if v == 2:
                count += 1
        if count == 1:
            high_card = False
            pair = True
        elif count > 1:
            high_card = False
            two_pair = True

    # Check trips
    if max(val_collector.values()) == 3:
        high_card = False
        trips = True

    # Check straight / straight flush / royal flush
    straight_num = 100
    straight_flush_num = 100
    for i in range(10):
        n = 0
        m = 0
        for x in straights[i]:
            if val_collector[x] > 0:
                n += 1
        if n > 4:
            straight_num = i
            straight = True
            trips = False
            pair = False
            two_pair = False
            high_card = False
            if max(suit_collector.values()) > 4:
                for each_card in self.hand:
                    if (each_card.str_card_repr[0] in straights[straight_num]
                    and each_card.str_card_repr[1] == suit_of_interest):
                        m += 1
            if m > 4:
                straight_flush_num = i
                straight_num = 100
                straight_flush = True
                straight = False
    if straight_flush_num == 9:
        royal = True
        straight_flush = False

    # Check flush
    if max(suit_collector.values()) >= 5 and not straight_flush and not royal:
        high_card = False
        pair = False
        two_pair = False
        trips = False
        flush = True

    # Check boat
    if 3 in val_collector.values() and not straight_flush and not royal:
        count = 0
        for v in val_collector.values():
            if v >= 2:
                count += 1
        if count >= 2:
            high_card = False
            trips = False
            flush = False
            boat = True

    # Check quads
    if max(val_collector.values()) == 4:
        high_card = False
        flush = False
        boat = False
        quads = True

    # Assembly
    if high_card:
        for j in range(10):
            self.five_card = self.hand[:5]
            outliers = self.hand[5:]
            for i, x in enumerate(self.five_card):
                if x.val < outliers[0].val:
                    a = self.five_card.pop(i)
                    self.five_card.insert(i, outliers[0])
                    outliers.pop(0)
                    outliers.insert(0, a)
            for i, x in enumerate(self.five_card):
                if x.val < outliers[1].val:
                    b = self.five_card.pop(i)
                    self.five_card.insert(i, outliers[1])
                    outliers.pop(1)
                    outliers.insert(1, b)
        for card in self.five_card:
            print(card.str_card_repr)
        print("high card")
        return self.five_card
    if pair:
        print("pair")
    if two_pair:
        print("two pair")
    if trips:
        print("trips")
    if straight:
        print("straight")
    if straight_flush:
        print("straight flush")
    if flush:
        print("flush")
    if quads:
        for k, v in val_collector.items():
            if v == 4:
                special = k
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] == special:
                self.five_card.append(x)
        self.five_card.append(self.hand[0])
        for i, card in enumerate(self.hand):
            if card.val > self.five_card[-1].val:
                self.five_card.pop(-1)
                self.five_card.append(card)
        print("quads")
        for card in self.five_card:
            print(card.str_card_repr)
        return self.five_card
    if boat:
        print("boat")
    if royal:
        print("royal")