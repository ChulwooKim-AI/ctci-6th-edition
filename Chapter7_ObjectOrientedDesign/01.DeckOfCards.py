"""Deck of Cards

Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.

Hints: 
#153
Note that a "card deck" is very broad. You might want to think about a reasonable scope
to the problem.
#275
How, if at all, will you handle aces?
"""

'''
Conditions:
Core objects:
Relationship:
Key actions:
'''

class Suit:
    def __init__(self):
        self.value = ['CLUB', 'SPADE', 'HEART', 'DIAMOND']
    
    def get_value(self, index):
        return self.value[index]
    

from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, face_value, suit):
        self.face_value = face_value
        self.suit = suit
        self.available = True
    
    @abstractmethod
    def value(self):
        pass

    def is_available(self):
        return self.available
    
    def mark_unavailable(self):
        self.available = False
    
    def mark_available(self):
        self.available = True
    

from random import randrange

class Deck:
    def __init__(self):
        self.dealt_index = 0
        self.cards = None

    def set_deck_of_cards(self, cards):
        self.cards = cards
    
    def shuffle(self):
        for i in range(len(self.cards)-1):
            random_index = randrange(i+1, len(self.cards))
            self.cards[i], self.cards[random_index] = self.cards[random_index], self.cards[i]
    
    def deal_hand(self, number):
        if self.remaining_cards() < number:
            return None
        hand = list()
        for i in range(number):
            card = self.deal_card()
            if card:
                hand[i] = card
        return hand
    
    def remaining_cards(self):
        return len(self.cards) - self.dealt_index
    
    def deal_card(self):
        if self.remaining_cards() == 0:
            return None
        card = self.cards[self.dealt_index]
        card.mark_unavailable()
        self.dealt_index += 1
        return card
    

class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def score(self):
        score = 0
        for card in self.cards:
            score += card.value()
        return score
    
    def add_card(self, card):
        self.cards.append(card)


class BlackJackCard(Card):
    def __init__(self, face_value, suit):
        super().__init__(face_value, suit)
    
    def value(self):
        if self.is_ace():
            return 1
        elif self.face_value >= 11 and self.face_value <= 13:
            return 10
        else:
            return self.face_value
    
    def min_value(self):
        return 1 if self.is_ace() else self.value()
    
    def max_value(self):
        return 11 if self.is_ace() else self.value() 

    def is_ace(self):
        return self.face_value == 1
    
    def is_face(self):
        return self.face_value >= 11 and self.face_value <= 13


import sys

class BlackJackHand(Hand):        
    def score(self):
        scores = self.possible_scores()
        max_under = -sys.maxsize - 1
        min_over = sys.maxsize
        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score <= 21 and score > max_under:
                max_under = score
        return min_over if max_under == -sys.maxsize - 1 else max_under
    
    def possible_scores(self):
        scores = list()
        if self.cards and len(self.cards) > 0:
            scores.append(0)
            for card in self.cards:
                for i in range(len(scores)):
                    if card.is_ace():
                        scores.append(scores[i]+card.max_value())
                    scores[i] += card.min_value()
        return scores
    
    def busted(self):
        return self.score() > 21
    
    def is_21(self):
        return self.score() == 21
    
    def is_blackjack(self):
        if len(self.cards) != 2:
            return False
        return (self.cards[0].is_ace() and self.cards[1].is_face()) or \
                (self.cards[1].is_ace() and self.cards[0].is_face())


class BlackJackGameAutomator:
    HIT_UNTIL = 16
    
    def __init__(self, number_of_players):
        self.deck = None
        self.hands = [BlackJackHand(list()) for _ in range(number_of_players)]
    
    def deal_initial(self):
        for hand in self.hands:
            card1 = self.deck.deal_card()
            card2 = self.deck.deal_card()
            if not (card1 and card2):
                return False
            hand.add_card(card1)
            hand.add_card(card2)
        return True
    
    def get_blackjack(self):
        winners = list()
        for idx, hand in enumerate(self.hands):
            if hand.is_blackjack():
                winners.append(idx)
        return winners
    
    def play_hand(self, index):
        while self.hands[index].score() < self.HIT_UNTIL:
            card = self.deck.deal_card()
            if card is None:
                return False
            self.hands[index].add_card(card)
        return True
    
    def play_all_hand(self):
        for i in range(len(self.hands)):
            if not self.play_hand(i):
                return False
        return True

    def get_winners(self):
        winners = list()
        winning_score = 0
        for i in range(len(self.hands)):
            if not self.hands[i].busted():
                if self.hands[i].score() > winning_score:
                    winning_score = self.hands[i].score()
                    winners.clear()
                    winners.append(i)
                elif self.hands[i].score() == winning_score:
                    winners.append(i)
        return winners
    
    def initialize_deck(self):        
        suit = Suit()
        cards = [BlackJackCard(i, suit.get_value(j)) for i in range(1, 14) for j in range(4)]
        self.deck = Deck()
        self.deck.set_deck_of_cards(cards)
        self.deck.shuffle()
            
    def print_hands_and_score(self):
        for idx, hand in enumerate(self.hands):
            print("Hand {} : ({})".format(idx, hand.score()))


if __name__ == "__main__":    
    automator = BlackJackGameAutomator(3)
    automator.initialize_deck()
    automator.deal_initial()
    automator.print_hands_and_score()
    blackjack = automator.get_blackjack()
    if blackjack and len(blackjack) > 0:
        print("Blackjack at", end=" ")
        for i in range(len(blackjack)-1):
            print(i, end=", ")
        print(blackjack[len(blackjack)-1])
    else:
        if automator.play_all_hand():
            print("Completed Game")
            automator.print_hands_and_score()
            winners = automator.get_winners()
            if len(winners) > 0:
                print("Winners :", end=" ")
                for i in range(len(winners)-1):
                    print(i, end=", "
                    )
                print(winners[len(winners)-1])
            else:
                print("Draw.")