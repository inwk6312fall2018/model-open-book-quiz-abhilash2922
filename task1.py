import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard
class PokerTable:

    def __init__(self, players:List[Player]):
        self.deck = pyCardDeck.Deck(
            cards=generate_deck(),
            name='Poker deck',
            reshuffle=False)
        self.players = players
        self.table_cards = []
        print("Created a table with {} players".format(len(self.players)))
def deal_cards(self, number: int):
    for _ in range(0, number):
        for player in self.players:
            card = self.deck.draw()
            player.hand.append(card)
            print("Dealt {} to player {}".format(card, player))
def flop(self):
    # Burn a card
    burned = self.deck.draw()
    self.deck.discard(burned)
    print("Burned a card: {}".format(burned))
    for _ in range(0, 3):
        card = self.deck.draw()
        self.table_cards.append(card)
        print("New card on the table: {}".format(card))
def river_or_flop(self):
    burned = self.deck.draw()
    self.deck.discard(burned)
    print("Burned a card: {}".format(burned))
    card = self.deck.draw()
    self.table_cards.append(card)
    print("New card on the table: {}".format(card))
def generate_deck() -> List[PokerCard]:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 'Ace',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine',
             '10': 'Ten',
             'J': 'Jack',
             'Q': 'Queen',
             'K': 'King'}
    cards = []
    for suit in suits:
        for rank, name in ranks.items():
            cards.append(PokerCard(suit, rank, name))
    print('Generated deck of cards for the table')
    return cards\
def main():
	player=PokerTable("player")
	pokerTable.flop()
	pokerTable.deal_cards()
	PokerTable.river_or_flop()
if __name__ == "__main__":
	main()

