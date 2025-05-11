from random import shuffle
class Card:
	suits = ["spade","heart","dia","club"]
	values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
	
	def __init__(self,s,v):
		self.suit = s
		self.value = v

	def __lt__(self,c1):
		if self.value < c1.value:
			return True 
		if self.value == c1.value:
			if self.suit < c1.suit:
				return True
			else:
				return False
		else:
			return False	

	def __gt__(self,c1):
		if self.value > c1.value:
			return True 
		if self.value == c1.value:
			if self.suit > c1.suit:
				return True
			else:
				return False
		else:
			return False	
	
	def __repr__(self):
		return "{} of {}".format(self.values[self.value],self.suits[self.suit])


class Deck:
	#まず52まいのカードを用意する
	cards = []

	def __init__(self):
		for i in range(2,15):
			for j in range(0,4):
				self.cards.append(Card(j,i))
		shuffle(self.cards)
	
	def rm_card(self):
		try:
			self.cards.pop()
		except IndexError:
			return None
			
	
class Player:
	def __init__(self,player):
		self.name = input("Enter players name".format(player))
		self.wins = 0
		

class Game:
	#ゲームを新しく始める
	def __init__(self):
		self.deck = Deck()

	#ゲームをスタートさせる。決着がつくまで実行し続ける	
	def play_game(self):
		p1 = Player("p1")
		p2 = Player("p2")
		de = self.deck
		while True:
			self.response = input("q to quit")
			if self.response == "q":
				break
			elif len(de.cards) < 2:
				print("no more cards")
				break
			else:
				#ドロー
				p1card = de.cards[len(de.cards)-1]
				print("{} has drawed {}".format(p1.name,p1card))
				de.rm_card()

				p2card = de.cards[len(de.cards)-1]
				print("{} has drawed {}".format(p2.name,p2card))
				de.rm_card()
				
				if p1card > p2card:
					p1.wins += 1
					print("{} has won this round".format(p1.name))
				else:
					p2.wins += 1
					print("{} has won this round".format(p2.name))
	
		if p1.wins > p2.wins:
			print("End of this game and {} won the game for winning {}times! of total {} times".format(p1.name,p1.wins,p1.wins+p2.wins))	
			
		if p1.wins < p2.wins:
			print("End of this game and {} won the game for winning {}times! of total {} times".format(p2.name,p2.wins,p1.wins+p2.wins))	
		

'''
ga = Game()
ga.play_game()
'''	


