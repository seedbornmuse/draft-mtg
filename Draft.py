


class Draft():

	def __init__(self, cards, max_players = 8, bots = True):
		self.players = []
		self.cards = cards
		self.max_players = max_players
		self.started = False
		
	def add_player(self, player):
		if not started and self.max_players > len(self.players):
			self.players.append(player)
			return True
		return False
		
	def remove_player(self, player)
		if player in self.players:
			self.players.remove(player)
			return True
		return False
	