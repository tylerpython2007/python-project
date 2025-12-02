import random

def whole_deck():
	suits=["hearts","diamonds","clubs","spades"] 
	numbered_cards = [
		("2", 2) ("3", 3) ("4", 4) ("5", 5) ("6", 6)
		("7", 7) ("8", 8) ("9", 0) ("10", 10)
		("jack", 10) ("queen", 10) ("king", 10)
	]

	deck=[]
	for suit in suits:
		for numbered_card, value in numbered_cards:
			deck.append([numbered_card,suit,vlaue])
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
def main():


if __name__ == "__maiun__":
	main()
