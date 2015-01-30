

class Draft():

	def __init__(self, cards, max_players = 8, bots = True):
		self.players = {} #{player:[packs]}
		self.cards = cards
		self.max_players = max_players
		self.started = False
		
	def add_player(self, player):
		if not started and self.max_players > len(self.players) and player not in self.players:
			self.players[player] = []
			return True
		return False
		
	def remove_player(self, player)
		if player in self.players:
			self.players.remove(player)
			return True
		return False
		
	def get_player(self, player):
		if player in self.players:
			return self.players[player]
		
	def start(self):
		if self.started:
			return False
			
		for player in self.players:
			self.players[player].append( generate_pack() )
		
		self.started = True
	
	
	def generate_pack(self):
		pass
		
		
		
class Player():
	def __init__(self, id, name=None):
		self.id = id
		self.deck = []
		self.packs = []
		self.draft = None
		