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


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def initialHand(self, deck):
        self.hand.append(deck.pop())
        self.hand.append(deck.pop())

    def hit(self, deck):
        print(f"{self.name} hits!")
        self.hand.append(deck.pop())

    def getHandValue(self):
        hand_value = sum(getCardValue(card) for card in self.hand)
        # Check for aces and adjust the hand value if necessary
        aces = self.getAcesCount()
        while hand_value > 21 and aces > 0:
            hand_value -= 10
            aces -= 1
        return hand_value

    def showHand(self):
        for card in self.hand:
            print(card["rank"], "of", card["suit"])
        # hand_value = sum(getCardValue(card) for card in self.hand)
        # print(f"{self.name}'s hand value is:", hand_value)

    def getAcesCount(self):
        return sum(card["rank"] == "Ace" for card in self.hand)


def shuffleDeck(deck):
    random.shuffle(deck)


def getCardValue(card):
    if card["rank"] == "Ace":
        return 11
    elif card["rank"] in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card["rank"])


def handleAction(action, player, deck):
    if action == "hit":
        player.hit(deck)
        # player.showHand()
        if player.getHandValue() > 21:
            # print("You lose!")
            return True
    elif action == "see":
        player.showHand()
    elif action == "stand":
        return True
    else:
        print("Please enter a valid action")
    print("Your hand value is:", player.getHandValue())
    return False


def startGame():
    wantToPlay = input("Do you want to play BLACKJACK? (y/n) ").lower()

    if wantToPlay != "y":
        return

    deck = createDeck()
    shuffleDeck(deck)

    p1 = Player("Player 1")
    p2 = Player("Player 2")

    p1.initialHand(deck)
    p2.initialHand(deck)

    while True:
        print()
        action = input("Do you want to hit, see, or stand? ")
        if handleAction(action, p1, deck):
            break

    if p1.getHandValue() <= 21:
        while p2.getHandValue() < 17:
            p2.hit(deck)

        # p1.showHand()
        p2.showHand()

        if p2.getHandValue() > 21:
            print("You win!")
        elif p2.getHandValue() > p1.getHandValue():
            print("You lose!")
        elif p2.getHandValue() < p1.getHandValue():
            print("You win!")
        else:
            print("You tied!")
    else:
        p1.getHandValue()
        print("You lose!")

    startGame()


startGame()
