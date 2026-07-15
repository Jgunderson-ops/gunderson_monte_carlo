import random
import time
#import numpy as np
#import pandas as pd
#import mathplotlib

class Player:
    """
    defense -> call / bluff frequency
        - loose, medium, tight
        INPUT -> L, M, or T
    offence -> bet size
        - Weak, Medium, Agressive
        INPUT -> W, M, A

    I understand that bluffing is offence, but it is more commonly associated
    with riskier play -- and fits with the attribute of calling
    """

    def __init__(
        self, name="", net_winnings=0, current_stack=50, play_style="N/N"
        ):

        # net winnings does not include stack
        self.net_winnings = net_winnings
        self.current_stack = current_stack
        self.hand = []
        self.five_card = []
        self.hand_val = 0
        self.still_in = False
        self.money_in_this_round = 0
        self.prev_stack = current_stack
        self.name = name
        self.special_seat = "not_special"
        self.straight_val = -1
        if play_style[0] == "L":
            self.defense = "loose"
        if play_style[0] == "M":
            self.defense = "medium"
        if play_style[0] == "T":
            self.defense = "tight"
        if play_style[2] == "W":
            self.offence = "weak"
        if play_style[2] == "M":
            self.offence = "medium"
        if play_style[2] == "A":
            self.offence = "agressive"

class Card:
    def __eq__(self, other):
        return isinstance(other, Card) and self.str_card_repr == other.str_card_repr
    def __hash__(self):
        return hash(self.str_card_repr)
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
            if str_card_repr[0] not in "0123456789jqka":
                raise ValueError(f"invalid card format: {str_card_repr}")
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

def make_fresh_deck():
    suits = ["h", "c", "s", "d"]
    vals = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "0", "j", "q", "k"]
    deck = []
    for i in suits:
        for j in vals:
            strin = j + i
            deck.append(Card(strin))
    return deck

def make_loose_possibilities():
    ldeck = make_fresh_deck()
    loose_pos = set()
    for i, icard in enumerate(ldeck):
        for j, jcard in enumerate(ldeck):
            # no dupe cards
            if icard == jcard:
                pass
            # no dupe hands
            elif (icard, jcard) in loose_pos or (jcard, icard) in loose_pos:
                pass
            # two cards 10+ get added
            elif icard.val > 9 and jcard.val > 9:
                loose_pos.add((icard, jcard))
            # pocket pairs
            elif icard.val == jcard.val:
                loose_pos.add ((icard, jcard))
            # suited aces get added
            elif icard.val == 15 and jcard.suit == icard.suit:
                loose_pos.add((icard, jcard))
            # suited connectors 4+ get added
            elif (
                    icard.val > 3 and
                    jcard.val == icard.val + 1 and
                    icard.suit == jcard.suit
                ):
                loose_pos.add((icard, jcard))
            elif icard.val + jcard.val > 18:
                loose_pos.add((icard, jcard))
    x = 1
    for h in loose_pos:
        x += 1
    #for card, card2 in loose_pos:
        #print(f"({card.str_card_repr}, {card2.str_card_repr}), {x}")
    #    x += 1
    return loose_pos

def make_med_possibilities():
    mdeck = make_fresh_deck()
    med_pos = set()
    for i, icard in enumerate(mdeck):
        for j, jcard in enumerate(mdeck):
            # no dupe cards
            if icard == jcard:
                pass
            # no dupe hands
            elif (icard, jcard) in med_pos or (jcard, icard) in med_pos:
                pass
            # two cards 10+ get added
            elif icard.val > 9 and jcard.val > 9:
                med_pos.add((icard, jcard))
            # pocket pairs
            elif icard.val == jcard.val:
                med_pos.add ((icard, jcard))
            # suited aces get added
            elif icard.val == 15 and jcard.suit == icard.suit:
                med_pos.add((icard, jcard))
            # suited connectors 4+ get added
            elif (
                    icard.val > 3 and
                    jcard.val == icard.val + 1 and
                    icard.suit == jcard.suit
                ):
                med_pos.add((icard, jcard))
            elif icard.val + jcard.val > 20:
                med_pos.add((icard, jcard))
    x = 1
    for card, card2 in med_pos:
        #print(f"({card.str_card_repr}, {card2.str_card_repr}), {x}")
        x += 1
    return med_pos

def make_tight_possibilities():
    tdeck = make_fresh_deck()
    tight_pos = set()
    for i, icard in enumerate(tdeck):
        for j, jcard in enumerate(tdeck):
            # no dupe cards
            if icard == jcard:
                pass
            # no dupe hands
            elif (icard, jcard) in tight_pos or (jcard, icard) in tight_pos:
                pass
            # two cards 10+ get added
            elif icard.val > 9 and jcard.val > 9:
                tight_pos.add((icard, jcard))
            # pocket pairs
            elif icard.val == jcard.val:
                tight_pos.add ((icard, jcard))
            # suited aces 7+ get added
            elif icard.val == 15 and jcard.suit == icard.suit and jcard.val > 6:
                tight_pos.add((icard, jcard))
            # suited connectors 8+ get added
            elif (
                    icard.val > 7 and
                    jcard.val == icard.val + 1 and
                    icard.suit == jcard.suit
                ):
                tight_pos.add((icard, jcard))
    x = 1
    for card, card2 in tight_pos:
        #print(f"({card.str_card_repr}, {card2.str_card_repr}), {x}")
        x += 1
    return tight_pos

def my_hand(self):
    """
    Protocol: default to high card, check if each hand is possible,
    then if it is, assemble the best hand given the hand they have.
    """
    self.five_card = []
    
    val_collector = {"a": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                     "8": 0, "9": 0, "0": 0, "j": 0, "q": 0, "k": 0}
    
    suit_collector = {"h": 0, "c": 0, "s": 0, "d": 0}
    
    straights = (
    "a2345", "23456", "34567", "45678", "56789",
    "67890", "7890j", "890jq", "90jqk", "0jqka"
            )
    
    for card in self.hand:
        val_collector[card.str_card_repr[0]] += 1
        suit_collector[card.str_card_repr[1]] += 1

    suit_of_interest = "z"
    for key, item in suit_collector.items():
        if item > 4:
            suit_of_interest = key
            break

    self.hand_val = 0
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
            self.hand_val = 1
        elif count > 1:
            high_card = False
            two_pair = True
            self.hand_val = 2

    # Check trips
    if max(val_collector.values()) == 3:
        high_card = False
        trips = True
        self.hand_val = 3

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
            self.straight_val = i
            straight = True
            trips = False
            pair = False
            two_pair = False
            high_card = False
            self.hand_val = 4
            if max(suit_collector.values()) > 4:
                for each_card in self.hand:
                    if (each_card.str_card_repr[0] in straights[straight_num]
                    and each_card.str_card_repr[1] == suit_of_interest):
                        m += 1
            if m > 4:
                straight_flush_num = i
                self.straight_val = i
                straight_num = 100
                straight_flush = True
                straight = False
                self.hand_val = 8
    if straight_flush_num == 9:
        royal = True
        straight_flush = False
        self.hand_val = 9

    # Check flush
    if max(suit_collector.values()) >= 5 and not straight_flush and not royal:
        high_card = False
        pair = False
        two_pair = False
        trips = False
        flush = True
        self.hand_val = 5

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
            self.hand_val = 6

    # Check quads
    if max(val_collector.values()) == 4:
        high_card = False
        flush = False
        boat = False
        quads = True
        self.hand_val = 7

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
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("high card")
        return self.five_card

    if pair:
        outliers = []
        for k, v in val_collector.items():
            if v == 2:
                special = k
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] == special:
                self.five_card.append(x)
            else:
                outliers.append(x)
        d = outliers.pop(0)
        s = outliers.pop(0)
        w = outliers.pop(0)
        self.five_card.append(d)
        self.five_card.append(s)
        self.five_card.append(w)
        for j in range(10):
            for i, x in enumerate(self.five_card):
                for c, h in enumerate(outliers):
                    if x.val < outliers[c].val and i > 1:
                        q = self.five_card.pop(i)
                        self.five_card.insert(i, outliers[c])
                        outliers.pop(c)
                        outliers.insert(c, q)
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("pair")
        return self.five_card

    if two_pair:
        outliers = []
        for k, v in val_collector.items():
            if v == 2:
                special = k
        for y, v in val_collector.items():
            if v == 2 and y != special:
                special2 = y
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] == special or x.str_card_repr[0] == special2:
                self.five_card.append(x)
            else:
                outliers.append(x)
        d = outliers.pop(0)
        self.five_card.append(d)
        for j in range(5):
            for i, x in enumerate(outliers):
                if x.val > self.five_card[-1].val:
                    self.five_card.pop(-1)
                    self.five_card.append(x)
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("two pair")
        return self.five_card

    if trips:
        outliers = []
        for k, v in val_collector.items():
            if v == 3:
                special = k
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] == special:
                self.five_card.append(x)
            else:
                outliers.append(x)
        d = outliers.pop(0)
        w = outliers.pop(0)
        self.five_card.append(d)
        self.five_card.append(w)
        for j in range(10):
            for i, x in enumerate(self.five_card):
                for c, h in enumerate(outliers):
                    if x.val < outliers[c].val and i > 2:
                        q = self.five_card.pop(i)
                        self.five_card.insert(i, outliers[c])
                        outliers.pop(c)
                        outliers.insert(c, q)
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("trips")
        return self.five_card

    if straight:
        cool_str = ""
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] in straights[straight_num] and (
                x.str_card_repr[0] not in cool_str):
                self.five_card.append(x)
                cool_str += x.str_card_repr[0]
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("straight")
        return self.five_card

    if straight_flush or royal:
        cool_str = ""
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] in straights[straight_flush_num] and (
                    x.str_card_repr[0] not in cool_str) and (
                    x.str_card_repr[1] == suit_of_interest):
                self.five_card.append(x)
                cool_str += x.str_card_repr[0]
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #if straight_flush:
        #    print("straight flush")
        #if royal:
        #    print("royal")
        return self.five_card

    if flush:
        outliers = []
        for i, x in enumerate(self.hand):
            if x.str_card_repr[1] == suit_of_interest:
                self.five_card.append(x)
        while len(self.five_card) > 5:
            d = self.five_card.pop(0)
            outliers.append(d)
        for j in range(10):
            for i, x in enumerate(self.five_card):
                for k, l in enumerate(outliers):
                    if l.val > x.val:
                        c = self.five_card.pop(i)
                        d = outliers.pop(k)
                        self.five_card.insert(i, d)
                        outliers.insert(k, c)
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("flush")
        return self.five_card

    if quads:
        for k, v in val_collector.items():
            if v == 4:
                special = k
        for i, x in enumerate(self.hand):
            if x.str_card_repr[0] == special:
                self.five_card.append(x)
        i = 0
        while len(self.five_card) == 4:
            if self.hand[i] not in self.five_card:
                self.five_card.append(self.hand[i])
            i += 1
        for _ in range(4):
            for i, card in enumerate(self.hand):
                if card.val > self.five_card[-1].val and (
                card.str_card_repr[0] != special):
                    self.five_card.pop(-1)
                    self.five_card.append(card)
        #print("quads")
        #for card in self.five_card:
        #    print(card.str_card_repr)
        return self.five_card

    if boat:
        threes = 0
        twos = 0
        s_3_1 = ("", 0)
        s_3_2 = ("", 0)
        s_2_1 = ("", 0)
        s_2_2 = ("", 0)
        s_2_3 = ("", 0)
        special_three = ""
        special_two = ""
        for k, v in val_collector.items():
            if v == 3:
                threes += 1
                if s_3_1 == ("", 0):
                    s_3_1 = (k, Card(k + "d").val)
                else:
                    s_3_2 = (k, Card(k + "d").val)
            if v == 2:
                twos += 1
                if s_2_1 == ("", 0):
                    s_2_1 = (k, Card(k + "d").val)
                elif s_2_2 == ("", 0):
                    s_2_2 = (k, Card(k + "d").val)
                else:
                    s_2_3 = (k, Card(k + "d").val)
        if s_3_2 == ("", 0):
            for card in self.hand:
                if card.str_card_repr[0] == s_3_1[0]:
                    self.five_card.append(card)
            s_3_1 = ("", 0)
        if s_3_2 != ("", 0):
            if s_3_1[1] > s_3_2[1]:
                for card in self.hand:
                    if card.str_card_repr[0] == s_3_1[0]:
                        self.five_card.append(card)
                s_3_1 = ("", 0)
            else:
                for card in self.hand:
                    if card.str_card_repr[0] == s_3_2[0]:
                        self.five_card.append(card)
                s_3_2 = ("", 0)
        cool_cool = max(
            s_3_1[1], s_3_2[1], s_2_1[1], s_2_2[1], s_2_2[1], s_2_3[1]
            )
        for card in self.hand:
            if card.val == cool_cool and len(self.five_card) < 5:
                self.five_card.append(card)
        #for card in self.five_card:
        #    print(card.str_card_repr)
        #print("boat")
        return self.five_card

def who_won(player_a, player_b):
    """
    figures out winner, returns a string.
    """

    if player_a.hand_val > player_b.hand_val:
        return "player_a"
    if player_b.hand_val > player_a.hand_val:
        return "player_b"

    a_val_collector = {"a": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                     "8": 0, "9": 0, "0": 0, "j": 0, "q": 0, "k": 0}
    b_val_collector = {"a": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                     "8": 0, "9": 0, "0": 0, "j": 0, "q": 0, "k": 0}

    for card in player_a.five_card:
        a_val_collector[card.str_card_repr[0]] += 1
    for card in player_b.five_card:
        b_val_collector[card.str_card_repr[0]] += 1

    # high card / flush
    if player_a.hand_val == 0 or player_a.hand_val == 5:
        a_others = []
        b_others = []
        for card in player_a.five_card:
            a_others.append(card.val)
        for card in player_b.five_card:
            b_others.append(card.val)
        for _ in range(5):
            a_max = max(a_others)
            b_max = max(b_others)
            a_others.remove(a_max)
            b_others.remove(b_max)
            if a_max > b_max:
                return "player_a"
            elif a_max < b_max:
                return "player_b"
        return "chop"
    
    # pair
    if player_a.hand_val == 1:
        p_a_pair_val = -1
        p_b_pair_val = -1
        a_others = []
        b_others = []
        for k, v in a_val_collector.items():
            if v == 2:
                p_a_pair_val = Card(k + "d").val
            else:
                a_others.append(Card(k + "d").val)
        for k, v in b_val_collector.items():
            if v == 2:
                p_b_pair_val = Card(k + "s").val
            elif v > 0:
                b_others.append(Card(k + "c").val)
        if p_a_pair_val > p_b_pair_val:
            return "player_a"
        elif p_a_pair_val < p_b_pair_val:
            return "player_b"
        for _ in range(3):
            a_max = max(a_others)
            b_max = max(b_others)
            a_others.remove(a_max)
            b_others.remove(b_max)
            if a_max > b_max:
                return "player_a"
            elif a_max < b_max:
                return "player_b"
        return "chop"
    
    # two pair
    if player_a.hand_val == 2:
        p_a_1 = -1
        p_a_2 = -1
        p_a_3 = -1
        p_b_1 = -1
        p_b_2 = -1
        p_b_3 = -1
        for k, v in a_val_collector.items():
            if v == 2:
                if p_a_1 == -1:
                    p_a_1 = Card(k + "d").val
                else:
                    p_a_2 = Card(k + "d").val
            elif v == 1:
                p_a_3 = Card(k + "c").val
        for k, v in b_val_collector.items():
            if v == 2:
                if p_b_1 == -1:
                    p_b_1 = Card(k + "s").val
                else:
                    p_b_2 = Card(k + "d").val
            elif v == 1:
                p_b_3 = Card(k + "d").val
        if max(p_a_1, p_a_2) > max(p_b_1, p_b_2):
            return "player_a"
        if max(p_a_1, p_a_2) < max(p_b_1, p_b_2):
            return "player_b"
        if min(p_a_1, p_a_2) > min(p_b_1, p_b_2):
            return "player_a"
        if min(p_a_1, p_a_2) < min(p_b_1, p_b_2):
            return "player_b"
        if p_a_3 > p_b_3:
            return "player_a"
        if p_a_3 < p_b_3:
            return "player_b"
        return "chop"

    # trips
    if player_a.hand_val == 3:
        p_a_trip_val = -1
        p_b_trip_val = -1
        a_others = []
        b_others = []
        for k, v in a_val_collector.items():
            if v == 3:
                p_a_trip_val = Card(k + "c").val
            else:
                a_others.append(Card(k + "s").val)
        for k, v in b_val_collector.items():
            if v == 3:
                p_b_trip_val = Card(k + "d").val
            else:
                b_others.append(Card(k + "d").val)
        if p_a_trip_val > p_b_trip_val:
            return "player_a"
        elif p_a_trip_val < p_b_trip_val:
            return "player_b"
        for _ in range(2):
            a_max = max(a_others)
            b_max = max(b_others)
            a_others.remove(a_max)
            b_others.remove(b_max)
            if a_max > b_max:
                return "player_a"
            elif a_max < b_max:
                return "player_b"
        return "chop"
    
    # straight
    if player_a.hand_val == 4:
        if player_a.straight_val == player_b.straight_val:
            return "chop"
        elif player_a.straight_val > player_b.straight_val:
            return "player_a"
        elif player_a.straight_val < player_b.straight_val:
            return "player_b"
    
    # boat
    if player_a.hand_val == 6:
        a_vals = [card.val for card in player_a.five_card]
        b_vals = [card.val for card in player_b.five_card]
        p_a_3 = max(set(a_vals), key=a_vals.count)
        p_a_2 = min(set(a_vals), key=a_vals.count)
        p_b_3 = max(set(b_vals), key=b_vals.count)
        p_b_2 = min(set(b_vals), key=b_vals.count)
        if p_a_3 > p_b_3:
            return "player_a"
        if p_a_3 < p_b_3:
            return "player_b"
        if p_a_2 > p_b_2:
            return "player_a"
        if p_a_2 < p_b_2:
            return "player_b"
        return "chop"

    # quads
    if player_a.hand_val == 7:
        p_a_4 = ""
        p_a_1 = ""
        p_b_4 = ""
        p_b_1 = ""
        for k, v in a_val_collector.items():
            if v == 4:
                p_a_4 = k
            if v == 1:
                p_a_1 = k
        for k, v in b_val_collector.items():
            if v == 4:
                p_b_4 = k
            if v == 1:
                p_b_1 = k
        if Card(p_a_4 + "h").val > Card(p_b_4 + "c").val:
            return "player_a"
        if Card(p_a_4 + "h").val < Card(p_b_4 + "s").val:
            return "player_b"
        if Card(p_a_1 + "h").val > Card(p_b_1 + "d").val:
            return "player_a"
        if Card(p_b_1 + "h").val < Card(p_b_1 + "d").val:
            return "player_b"
        return "chop"

    # straight flush
    if player_a.hand_val == 8:
        if player_a.straight_val == player_b.straight_val:
            return "chop"
        elif player_a.straight_val > player_b.straight_val:
            return "player_a"
        elif player_a.straight_val < player_b.straight_val:
            return "player_b"
    
    # royal
    if player_a.hand_val == 9:
        return "chop"

def find_odds_chevy(player_a_hand, player_b_play_style, board):
    import time
    trials = 1000
    preflop = False
    flop = False
    turn = False
    start = time.perf_counter()
    deck_h = make_fresh_deck()
    wins = 0
    ties = 0
    losses = 0
    a_clone = Player()
    b_clone = Player()
    a_clone.hand = player_a_hand[:]
    if player_b_play_style == "loose":
        x = make_loose_possibilities()
    elif player_b_play_style == "medium":
        x = make_med_possibilities()
    elif player_b_play_style == "tight":
        x = make_tight_possibilities()
    elif player_b_play_style == "all_combos":
        x = all_card_combos()
    hand_set = list(x)
    for _ in range(trials):
        b_clone.hand = board[:]
        each_hand = hand_set[random.randint(0, len(hand_set) - 1)]
        while each_hand[0] in a_clone.hand or each_hand[1] in a_clone.hand:
            each_hand = hand_set[random.randint(0, len(hand_set) - 1)]
        b_clone.hand.append(each_hand[0])
        b_clone.hand.append(each_hand[1])
        if len(board) == 0:
            card1 = deck_h[random.randint(0, 51)]
            card2 = deck_h[random.randint(0, 51)]
            card3 = deck_h[random.randint(0, 51)]
            card4 = deck_h[random.randint(0, 51)]
            card5 = deck_h[random.randint(0, 51)]
            ddd = [card1, card2, card3, card4, card5]
            w = {}
            for card in ddd:
                if card not in w:
                    w[card] = 0
                else:
                    w[card] += 1
            while (
                card1 in a_clone.hand or
                card2 in a_clone.hand or
                card3 in a_clone.hand or
                card4 in a_clone.hand or
                card5 in a_clone.hand or
                max(w.values()) > 1
            ):
                card1 = deck_h[random.randint(0, 51)]
                card2 = deck_h[random.randint(0, 51)]
                card3 = deck_h[random.randint(0, 51)]
                card4 = deck_h[random.randint(0, 51)]
                card5 = deck_h[random.randint(0, 51)]
                ddd = [card1, card2, card3, card4, card5]
                w = {}
                for card in ddd:
                    if card not in w:
                        w[card] = 0
                    else:
                        w[card] += 1
            a_clone.hand.append(card1)
            a_clone.hand.append(card2)
            a_clone.hand.append(card3)
            a_clone.hand.append(card4)
            a_clone.hand.append(card5)
            b_clone.hand.append(card1)
            b_clone.hand.append(card2)
            b_clone.hand.append(card3)
            b_clone.hand.append(card4)
            b_clone.hand.append(card5)
            preflop = True
        elif len(board) == 3:
            card1 = deck_h[random.randint(0, 51)]
            card2 = deck_h[random.randint(0, 51)]
            while (
                card1 in a_clone.hand or
                card2 in a_clone.hand or
                card1 == card2
                ):
                card1 = deck_h[random.randint(0, 51)]
                card2 = deck_h[random.randint(0, 51)]
            a_clone.hand.append(card1)
            a_clone.hand.append(card2)
            b_clone.hand.append(card1)
            b_clone.hand.append(card2)
            flop = True
        elif len(board) == 4:
            card1 = deck_h[random.randint(0, 51)]
            while card1 in a_clone.hand:
                card1 = deck_h[random.randint(0, 51)]
            a_clone.hand.append(card1)
            b_clone.hand.append(card1)
            turn = True
        try:
            my_hand(a_clone)
            my_hand(b_clone)
            super_super_cool = who_won(a_clone, b_clone)
            if super_super_cool == "player_a":
                wins += 1
            elif super_super_cool == "player_b":
                losses += 1
            elif super_super_cool == "chop":
                ties += 1
        except Exception as e:
            pass
        if preflop:
            for _ in range(5):
                a_clone.hand.pop(-1)
                b_clone.hand.pop(-1)
        if flop:
            for _ in range(2):
                a_clone.hand.pop(-1)
                b_clone.hand.pop(-1)
        if turn:
            a_clone.hand.pop(-1)
            b_clone.hand.pop(-1)
    end = time.perf_counter()
    #print("Elapsed:", end - start, "seconds")
    #return f"wins={wins}, ties={ties}, losses={losses} wp = {wins / trials} tp = {ties / trials} lp = {losses / trials}"
    #print(f"WP: {wins / trials}")
    #print(f"TP: {ties / trials}")
    #print(f"LP: {losses / trials}")
    return ((wins / trials) - (losses / trials))

def all_card_combos():
    adeck = make_fresh_deck()
    all_set = set()
    for i, icard in enumerate(adeck):
        for j, jcard in enumerate(adeck):
            if icard == jcard:
                pass
            elif (icard, jcard) in all_set or (jcard, icard) in all_set:
                pass
            else:
                all_set.add((icard, jcard))
    return all_set

def all_card_combos_ranked():
    x = all_card_combos()
    all_combos = list(x)
    ranked_hands = []
    for combo in all_combos:
        unidentified = Player()
        unidentified.hand.append(combo[0])
        unidentified.hand.append(combo[1])
        d = find_odds_chevy(unidentified.hand, "all_combos", [])
        ranked_hands.append((f"{combo[0].str_card_repr}/{combo[1].str_card_repr}", d))
    ranked_sorted = sorted(ranked_hands, key=lambda x: x[1], reverse=True)
    return ranked_sorted

def find_odds_ferrari(player_a_hand, player_b_play_style, board):
    """
    many modifications must be made
    """
    deck_h = make_fresh_deck()
    wins = 0
    ties = 0
    losses = 0
    a_clone = Player()
    b_clone = Player()
    a_clone.hand = player_a_hand[:]
    if player_b_play_style == "loose":
        x = make_loose_possibilities()
    elif player_b_play_style == "medium":
        x = make_med_possibilities()
    elif player_b_play_style == "tight":
        x = make_tight_possibilities()
    if len(board) == 3:
        for each_hand in x:
            b_clone.hand = board[:]
            if each_hand[0] in a_clone.hand or each_hand[1] in a_clone.hand:
                pass
            else:
                b_clone.hand.append(each_hand[0])
                b_clone.hand.append(each_hand[1])
                for card1 in deck_h:
                    for card2 in deck_h:
                        if (
                            card1 in a_clone.hand or
                            card2 in a_clone.hand or
                            card1 == card2
                            ):
                            pass
                        else:
                            a_clone.hand.append(card1)
                            a_clone.hand.append(card2)
                            b_clone.hand.append(card1)
                            b_clone.hand.append(card2)
                            my_hand(a_clone)
                            my_hand(b_clone)
                            h = who_won(a_clone, b_clone)
                            if h == "player_a":
                                wins += 1
                            elif h == "player_b":
                                losses += 1
                            elif h == "chop":
                                ties += 1
                            a_clone.hand.pop(-1)
                            a_clone.hand.pop(-1)
                            b_clone.hand.pop(-1)
                            b_clone.hand.pop(-1)
        return f"wins={wins}, ties={ties}, losses={losses}"

def find_pot_odds(call_cost, pot_size):
    return call_cost / (pot_size + call_cost)

def how_many_in_pot(p_list):
    x = 0
    for player in p_list:
        if player.still_in:
            x += 1
    return x

def are_all_players_compliant(dict_for_comp):
    for k, v in dict_for_comp:
        if not v:
            return False
    return True

def opp_player_makeup(caller, p_list):
    loose = 0
    medium = 0
    tight = 0
    for player in p_list:
        if player.still_in and player != caller:
            if player.defense == "loose":
                loose += 1
            elif player.defense == "medium":
                medium += 1
            elif player.defense == "tight":
                tight += 1
    return (loose, medium, tight)

def the_big_game(players_list, num_nights, num_hands_per_night, buy_in_val):
    """
    Initialize players that you want around the table and put them in a list.
    The loop will choose their seating arrangement and the rest. 
    """
    night_counter = 0
    hands_played_tonight = 0
    loose_pos = make_loose_possibilities()
    med_pos = make_med_possibilities()
    tight_pos = make_tight_possibilities()
    while night_counter < num_nights:
        while hands_played_tonight < num_hands_per_night:
            # remembering order of players and rotating the button
            order_for_next_game = players_list[:]
            a = order_for_next_game.pop(0)
            order_for_next_game.append(a)
            
            # initialize game / deal cards
            compliance_dict = {}
            game_board = []
            for player in players_list:
                player.still_in = True
                player.hand = []
                player.five_card = []
                player.hand_val = 0
                p_l = []
                player.money_in_this_round = 0
                player.straight_val = -1
            
            official_deck = make_fresh_deck()
            random.shuffle(official_deck)
            pot = 0
            needed_bet = 2
            for _ in range(2):
                for i, player in enumerate(players_list):
                    new_card = official_deck.pop(random.randint(0, 20))
                    player.hand.append(new_card)
                    if i == 0:
                        player.special_seat = "dealer"
                        compliance_dict[player.name] = False
                    elif i == 1:
                        player.special_seat = "small_blind"
                        compliance_dict[player.name] = False
                    elif i == 2:
                        player.special_seat = "big_blind"
                        compliance_dict[player.name] = True
                    else:
                        player.special_seat = "not_special"
                        compliance_dict[player.name] = False
            for i, player in enumerate(players_list):
                if player.special_seat == "small_blind":
                    player.money_in_this_round = 1
                    player.current_stack -= 1
                    pot += 1
                if player.special_seat == "big_blind":
                    player.money_in_this_round = 2
                    player.current_stack -= 2
                    pot += 2
                if player.current_stack < 2:
                    player.current_stack += buy_in_val
                    player.net_winnings -= buy_in_val
                player.prev_stack = player.current_stack
            # preflop
            for i, player in enumerate(players_list):
                if player.defense == "loose":
                    if (
                        (player.hand[0], player.hand[1]) in loose_pos or
                        (player.hand[1], player.hand[0]) in loose_pos or
                        player.money_in_this_round == needed_bet or
                        find_pot_odds((needed_bet - player.money_in_this_round), pot) >= find_odds_chevy(player.hand, "loose", [])):
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} in")
                        for card in player.hand:
                            print(card.str_card_repr)
                    else:
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} out")
                        for card in player.hand:
                            print(card.str_card_repr)
                if player.defense == "medium":
                    if (
                    (player.hand[0], player.hand[1]) in med_pos or
                    (player.hand[1], player.hand[0]) in med_pos or
                    player.money_in_this_round == needed_bet or
                    find_pot_odds((needed_bet - player.money_in_this_round), pot) >= find_odds_chevy(player.hand, "medium", [])):
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} in")
                        for card in player.hand:
                            print(card.str_card_repr)
                    else:
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} out")
                        for card in player.hand:
                            print(card.str_card_repr)
                if player.defense == "tight":
                    if (
                    (player.hand[0], player.hand[1]) in tight_pos or
                    (player.hand[1], player.hand[0]) in tight_pos or
                    player.money_in_this_round == needed_bet or
                    find_pot_odds((needed_bet - player.money_in_this_round), pot) >= find_odds_chevy(player.hand, "tight", [])):
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} in")
                        for card in player.hand:
                            print(card.str_card_repr)
                    else:
                        print("|||||||||||||||||||||||||||")
                        print(f"{player.name} out")
                        for card in player.hand:
                            print(card.str_card_repr)
            print("________________________________________")
            print(pot)
            night_counter += 1
            hands_played_tonight += 1