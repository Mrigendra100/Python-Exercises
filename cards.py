#  This example will make use of OOPs concept to shuffle cards

from random import shuffle

# Define a class to create all types of cards

class Cards:
    global suites , values
    suites = ['Hearts' , 'Diamonds' , 'Clubs' , 'Spades' ]
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        pass

# Define class for category

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.mycardset=[]
        for n in suites:
            for c in values:
                self.mycardset.append((c) + " " + "of"+" "+n )

    # for popping the card method
    def popCard(self):
        if len(self.mycardset) == 0:
            return "No Cards can be popped further"
        
        else:
            cardpopped = self.mycardset.pop()
            print("Popped card is" , cardpopped)


#  class to shuffle the deck of cards

class ShuffleCards(Deck):
    def __init__(self):
        Deck.__init__(self)

    # method to shuffle cards
    def shuffle(self):
        if len(self.mycardset) < 52:
            print("cannot shuffle the cards")
        else:
            shuffle(self.mycardset)
            return self.mycardset


objCards = Cards()
objDeck = Deck()

mycards = objDeck.mycardset


print('\n Mrigendra Cards: \n', mycards)

objShufflecards = ShuffleCards()

print('\n Cards after shuffling:' , objShufflecards.shuffle())

