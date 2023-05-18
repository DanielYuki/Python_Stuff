import random


# Create a deck of 52 cards
def createDeck():
    deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]

    for suit in suits:
        for rank in ranks:
            deck.append({"rank": rank, "suit": suit})

    return deck


deck = createDeck()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def initialHand(self):
        self.hand.append(deck.pop())
        self.hand.append(deck.pop())

    def hit(self):
        print("You hit!")
        self.hand.append(deck.pop())

    def getHandValue(self):
        sum = 0
        for card in self.hand:
            sum += getCardValue(card)
        return sum

    def showHand(self):
        for card in self.hand:
            print(self.name + ": " + card["rank"] + " of " + card["suit"])


hand = []


def shuffleDeck(deck):
    random.shuffle(deck)


def getCardValue(card):
    if card["rank"] == "Ace":
        return 11
    elif card["rank"] in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card["rank"])


p1 = Player("Player 1")
p2 = Player("Player 2")


def handleAction(action):
    if action == "hit":
        p1.hit()
        p1.showHand()
        if p1.getHandValue() > 21:
            print("You lose!")
            startGame()
    elif action == "see":
        p1.showHand()
    elif action == "stand":
        while p2.getHandValue() < 17:
            p2.hit()
        if p2.getHandValue() > 21:
            print("You win!")
            startGame()
        elif p2.getHandValue() > p1.getHandValue():
            print("You lose!")
            startGame()
        elif p2.getHandValue() < p1.getHandValue():
            print("You win!")
            startGame()
        elif p2.getHandValue() == p1.getHandValue():
            print("You tied!")
            startGame()
    else:
        print("Please enter a valid action")

    print("Your hand value is: " + str(p1.getHandValue()))


# game starts here
def startGame():
    wantToPlay = input("Do you want to play BLACKJACK? (y/n) ")

    if wantToPlay.lower() != "y":
        return

    shuffleDeck(deck)
    p1.initialHand()
    p2.initialHand()

    while True:
        action = input("Do you want to hit, see or stand? ")
        handleAction(action)


startGame()
