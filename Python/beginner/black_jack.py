import random

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades","clubs","hearts","diamonds"]
        ranks = [
            {"rank":"A","value":11},
            {"rank":"2","value":2},
            {"rank":"3","value":3},
            {"rank":"4","value":4},
            {"rank":"5","value":5},
            {"rank":"6","value":6},
            {"rank":"7","value":7},
            {"rank":"8","value":8},
            {"rank":"9","value":9},
            {"rank":"10","value":10},
            {"rank":"J","value":10},
            {"rank":"Q","value":10},
            {"rank":"K","value":10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        if len(self.cards)>1:
            return random.shuffle(self.cards)

    def deal(self,num):
        dealt_cards = []
        for i in range(num):
            if len(self.cards)>0:
                card = self.cards.pop()
                dealt_cards.append(card)
        return dealt_cards

class Hand:
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer

    def add_card(self,new_cards):
        self.cards.extend(new_cards)

    def calculate_value(self):
        self.value=0
        ace_found=False
        for card in self.cards:
            card_value=int(card.rank["value"])
            self.value+=card_value
            if card.rank["rank"]=="A":
                ace_found=True
        if ace_found and self.value>21:
            self.value-=10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value()==21

    def display(self,show_all_dealer_cards=False):
        print(f'{"Dealer" if self.dealer else "Your"} cards:')
        for index,card in enumerate(self.cards):
            if index==0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden card")
            else:
                print(card)
        if not self.dealer:
            print("Total:",self.get_value())
        print()

class Game:
    def play(self):
        game_count = 0
        total_games = 0
        while total_games <= 0:
            try:
                total_games = int(input("How many games? "))
            except:
                print("Enter a number")

        while game_count < total_games:
            game_count += 1

            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_count} of {total_games}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand,dealer_hand):
                continue

            choice=""
            while player_hand.get_value()<21 and choice not in ["s","stand"]:
                choice=input("Hit or Stand? ").lower()
                print()
                while choice not in ["h","s","hit","stand"]:
                    choice=input("Enter H or S: ")
                    print()
                if choice in ["hit","h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand,dealer_hand):
                continue

            player_value=player_hand.get_value()
            dealer_value=dealer_hand.get_value()

            while dealer_value<17:
                dealer_hand.add_card(deck.deal(1))
                dealer_value=dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand,dealer_hand):
                continue

            print("Final result")
            print("Your score:",player_value)
            print("Dealer score:",dealer_value)
            self.check_winner(player_hand,dealer_hand,True)

        print("\nThanks for playing!")

    def check_winner(self,player_hand,dealer_hand,game_over=False):
        if not game_over:
            if player_hand.get_value()>21:
                print("You busted. Dealer wins")
                return True
            elif dealer_hand.get_value()>21:
                print("Dealer busted. You win")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both got blackjack. Tie")
                return True
            elif player_hand.is_blackjack():
                print("You got blackjack. You win")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer got blackjack. Dealer wins")
                return True
        else:
            if player_hand.get_value()>dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value()==dealer_hand.get_value():
                print("Its a tie")
            else:
                print("Dealer wins")
            return True
        return False

game=Game()
game.play()