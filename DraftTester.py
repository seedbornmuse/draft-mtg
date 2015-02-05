from Draft import Draft


def testAddRemove(d):
	print d.players
	print 'Add 0: ', d.add_player('0')
	print d.players
	print 'Add 1: ', d.add_player('1')
	print d.players
	print 'Add 1: ', d.add_player('1')
	print d.players
	print 'Add 2: ', d.add_player('2')
	print 'Add 3: ', d.add_player('3')
	print 'Add 4: ', d.add_player('4')
	print 'Add 5: ', d.add_player('5')
	print 'Add 6: ', d.add_player('6')
	print 'Add 7: ', d.add_player('7')
	print len(d.players)
	print 'Add 8: ', d.add_player('8')
	print len(d.players)

	print ''
	
	print 'Remove 0: ', d.remove_player('0')
	print len(d.players)
	print 'Remove 0: ', d.remove_player('0')
	print len(d.players)
	print 'Add 0: ', d.add_player('0')
	print len(d.players)
	
	return d
	
def testDraft():

	d = Draft(['1','2','3','4','5'], max_players=4)

	players = 4
	for i in range(players - 1):
		d.add_player( str(i) )
		
	#print d.players
	#for player in d.players:
	#	print player
	
	d.start()
	
	for player in d.players:
		print player, ': ', player.pack_queue[0]
	
def main():
	#d = Draft('1,2,3,4,5')
	#testAddRemove(d)

	testDraft()



if __name__ == "__main__":
    main()