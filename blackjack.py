import random
from db import read_money, money_to_txt

def whole_deck():
	suits=["hearts","diamonds","clubs","spades"] 
	numbered_cards = [
		("Ace", 11),
		("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
		("7", 7), ("8", 8), ("9", 0), ("10", 10),
		("jack", 10), ("queen", 10), ("king", 10)
	]

	deck=[]
	for suit in suits:
		for numbered_card, value in numbered_cards:
			deck.append([numbered_card,suit,value])
	return deck

def hand_number(hand):
	value = 0
	aces = 0


	for card in hand:
		value += card[2]
		if card[0] == "Ace":
			aces += 1

	while value > 21 and aces > 0:
		value -=10
		aces -= 1
	return value
def in_hand(hand):
	text=" "
	for numbered_card,suit, _ in hand:
		if text != "":
			text += ", "
		text += (f"{numbered_card} of {suit}")
	return text
	

def main():
	print("blackjack")
	print("blackjack payout is 3:2")

	money = read_money
	print(f"Money: {money}")


#minimum and  maximum bets
	while True:
		try:
			bet = float(input("Bet amount:  "))
			if bet < 5:
				print("Minimum bet is 5")
			elif bet > 1000:
				print("maximum bet is 1000")
			elif bet > money:
				print("you not have enough money to bet this amount")
			else:
				break
		except ValueError:
			print("Invald number try again")

#deal card

	deck = whole_deck
	player = [deck.pop(), deck.pop()]
	dealer = [deck.pop(), deck.pop()]
	
	print()
	print("dealers cards: ")
	print(f"{dealer[0][0]} of {dealer[0][2]}")
	print()
	print("your cards: ")
	print(in_hand(player))
	
#player
	while True:
		print()
		choice = input("hit or stand? (hit/stand):  ")
		if choice == "hit":
			player.append(deck.pop())
			print("your card: ")
			print(in_hand(player))
			if hand_number(player) > 21
				break
		elif choice == stand;
			break
		else:
			print("invalid choice")

	player_total = hand_number(player)
#dealer




if __name__ == "__main__":
	main()
