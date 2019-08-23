# __init__ usage
# __init__ the double __ means it is private
#  init is triggered when class is instantiated
class Card:
    # Define the suits
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4
    SUITS = {
        CLUBS: 'Clubs',
        HEARTS: 'Hearts',
        DIAMONDS: 'Diamonds',
        SPADES: 'Spades'
    }
 
    # Define the names of special cards
    VALUES = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
 
    def __init__(self, suit, value):
        # Save the suit and card value
        self.suit = suit
        self.value = value

    def lt(self, other):
        # Compare the card with another card
        # (return true if we are smaller, false if
        # we are larger, 0 if we are the same)
        # card = Card(0,1)
        # card3 = Card(0, 1)
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
 
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False

        return 0
 
    def str(self):
        # Return a string description of ourself
        if self.value in self.VALUES:
            buf = self.VALUES[self.value]
        else:
            buf = str(self.value)
        buf = buf + ' of ' + self.SUITS[self.suit]
 
        return buf

card = Card(0,1)
card3 = Card(2, 3)
print(card.lt(card3))
