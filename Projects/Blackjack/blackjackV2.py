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


# Create a player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Get the initial hand of the player (two cards)
    def initialHand(self, deck):
        self.hand.append(deck.pop())
        self.hand.append(deck.pop())

    # Get a new card from the deck
    def hit(self, deck):
        print(f"{self.name} hits!")
        self.hand.append(deck.pop())

    # Get the value of the player's hand
    def getHandValue(self):
        hand_value = sum(getCardValue(card) for card in self.hand)
        # Check for aces and adjust the hand value if necessary
        # (I think aces do that now...)
        aces = self.getAcesCount()
        while hand_value > 21 and aces > 0:
            hand_value -= 10
            aces -= 1
        return hand_value

    # Show the player's hand
    def showHand(self):
        for card in self.hand:
            print(card["rank"], "of", card["suit"])

    # Get the number of aces in the player's hand
    def getAcesCount(self):
        return sum(card["rank"] == "Ace" for card in self.hand)


# Shuffle the deck
def shuffleDeck(deck):
    random.shuffle(deck)


# Get the value of a card
def getCardValue(card):
    if card["rank"] == "Ace":
        return 11
    elif card["rank"] in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card["rank"])


# Handle the player's action
def handleAction(action, player, deck):
    if (action == "hit" or action == "h"):
        player.hit(deck)
        if player.getHandValue() > 21:
            return True
    elif (action == "view" or action == "v"):
        player.showHand()
    elif (action == "stand" or action == "s"):
        return True
    else:
        print("\n", "Please enter a valid action", "\n")
    print("Your hand value is:", player.getHandValue())
    return False


# Start the game function
def startGame():
    wantToPlay = input("Do you want to play BLACKJACK? (y/n) ").lower()

    if wantToPlay != "y":
        return

    deck = createDeck()
    shuffleDeck(deck)

    # Bronco p krl
    p1 = Player("Player 1")
    p2 = Player("Player 2")

    p1.initialHand(deck)
    p2.initialHand(deck)

    print(" Your hand is: ")
    p1.showHand()
    print("\n", "Your opponent has a: " + str(p2.hand[0]['rank']) +
          " of " + str(p2.hand[0]['suit']), "\n")

    while True:
        print()
        action = input("Do you want to hit(h), view hand(v), or stand(s)? ")
        if handleAction(action, p1, deck):
            break

    if p1.getHandValue() <= 21:
        while p2.getHandValue() < 17:
            p2.hit(deck)

        # p1.showHand()
        print("\n", "Your opponent's hand is: ")
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
        print("\n", "Your hand is: ")
        p1.showHand()
        print("Your hand value is: ", p1.getHandValue())
        print("\n", "You lose!")

    startGame()


startGame()
