# In-terminal 'pairs' player using expected best outcome at each move.
# http://cheapass.com/pairs/

def newDeck():
	L = []
	for i in xrange(1, 11):
		for j in xrange(0, i):
			L.append(i)
	return L

# Methods used to play pairs for a single player
class Game:
	def __init__(self, cards, table, maxPoints, variation):
		self.cards = cards
		self.table = table
		self.possible = newDeck()
		self.maxPoints = maxPoints
		self.points = 0
		self.variation = variation

	# Methods which change the state of the board
	def shuffle(self):
		L = newDeck()
		for e in (self.table):
			L.remove(e)
		return L

	def addCardToTable(self, e):
		(self.table).append(e)
		(self.possible).remove(e)

	def addCardToPlayer(self, e):
		(self.cards).append(e)
		(self.table).append(e)
		(self.possible).remove(e)

	def newHand(self):
		self.cards = []
		self.table = []

	# Methods used to decide whether to hit or fold in a given situation.
	# Done by choosing the option with the lower amount of expected points. 
	def hitValue(self, e):
		cards = self.cards
		if (len(cards) == 0):
			return 0
		elif ((self.variation) and (cards[len(cards) - 1] + e == 10)): 
			if (e == 5): 
				return min(e, self.maxPoints - self.points)
			else:
				return min(10, self.maxPoints - self.points)
		else:
			for c in cards:
				if (c == e):
					return min(e, self.maxPoints - self.points)
		return 0

	def hitOrFold(self):
		if (len(self.table) != 0):
			foldPoints = min(self.table)
		else:
			foldPoints = 0
		possible = self.possible
		n = float(len(possible))
		individualHits = map(lambda e: self.hitValue(e), possible)
		individualExpectedHits = map(lambda e: e/n, individualHits)
		expectedHit = reduce(lambda x, y: x + y, individualExpectedHits)
		print "expected hit:", expectedHit, "fold:", foldPoints
		return (expectedHit <= foldPoints)

# Initialization
variant = True
game = Game([], [], 16, variant)

# Input loop
while True:
	command = raw_input("> ")
	if (command == ""): continue
	elif (command == "exit"): break
	elif (command == "shuffle"): game.shuffle()
	elif (command == "new hand"): game.newHand()
	elif (command == "p"):
		val = raw_input("Which card? > ")
		if (val == ""): continue
		game.addCardToPlayer(int(val))
	elif (command == "t"):
		val = raw_input("Which card? > ")
		if (val == ""): continue
		game.addCardToTable(int(val))
	elif (command == "points"):
		val = raw_input("How many points? > ")
		if (val == ""): continue
		game.points += int(val)
	elif (command == "?"):
		if (game.hitOrFold()):
			print "Hit."
		else:
			print "Fold."
	elif (command == "status"):
		print "My cards are", game.cards, "..."
		print "The cards on the table are", game.table, "..."
		print "I have", game.points, "points ..."
