import random

class Draft():

	def __init__(self, cards, max_players = 8, bots = True, pack_size=15):
		self.players = [] #{id:Player obj}
		self.cards = cards
		self.max_players = max_players
		self.pack_size = pack_size
		
		self.started = False
		
		
	def add_player(self, playerID):
		if self.started:
			return False
	
		if self.max_players > len(self.players) and self.get_player(playerID) is None:
			self.players.append( Player(playerID) )
			return True
			
		return False
		
		
	#Add logic for creating bot if player drops
	def remove_player(self, playerID):
		player = self.get_player(playerID)
		if player is not None:
			if self.started:
				return False
			else:
				self.players.remove(player)
				return True
		return False
		
		
	def get_player(self, playerID):
		for player in self.players:
			if playerID == player.id:
				return player
		return None
			
		
	def generate_pack(self):
		#if self.pack_size < len(self.cards):
		#	return None
	
		pack = []
		for i in range( min(self.pack_size, len(self.cards)) ):
			num = random.randint(0, len(self.cards) - 1)
			pack.append(self.cards.pop(num))
			
		return pack
		
		
	def start(self):
		if self.started:
			return False
		
		for i in range(self.max_players - len(self.players)):
			self.players.append( Bot(str(i)) )
			
		random.shuffle(self.players)
		
		for player in self.players:
			pack = self.generate_pack()
			if pack is not None:
				player.pack_queue.append( pack )
		
		self.started = True
		
		#notify()
	
		return True

		
	def update(self, playerID, pick_index): #, notify_func):
		#updated = False
	
		if playerID in self.players and self.started:
			player = self.players[playerID]
			
			try:
				pack = player.pack_queue[0]
				card = pack[pick_index]
				player.deck.append(card)
				player.pack_queue.pop(0)
				
				#pass()
				next = self.table_order.index(playerID)
				next.pack_queue.append(pack)
				
				#itertools to reverse list
				while next.isbot():
					pass
					
				#updated = True
			except IndexError:
				pass
		
		data = "data"
		
		return data
		
		
#dentist
		
class Player():
	def __init__(self, id, name=None):
		self.id = id
		self.deck = []
		self.pack_queue = []
		self.draft = None
	
	def is_bot(self):
		return False
		
	def __str__(self):
		return 'player'
		
class Bot(Player):
	def __init__(self, id):
		Player.__init__(self,"bot" + str(id))

	def is_bot(self):
		return True
		
	def __str__(self):
		return 'bot'
		

		