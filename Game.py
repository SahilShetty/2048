import random

from math import ceil


def zPush(scape, ending, nextVal, repeat = 0): # zPush = Zero Push; scape = landscape (horizontal and vertical) - pun

	repeat += 1

	for zero in ending:

		if scape[zero] == 0:

			scape[zero] = scape[zero + nextVal]

			scape[zero + nextVal] = 0

	if repeat <= 4: zPush(scape, ending, nextVal, repeat)

	return scape


def sPush(scape, ending, nextVal): # sPush = Same Push

	scape = zPush(scape, ending, nextVal)

	for same in ending:

		if scape[same] == scape[same + nextVal] and scape[same] != 0:

			scape[same] *= 2

			scape[same + nextVal] = 0

	scape = zPush(scape, ending, nextVal)

	return scape


def vertical(ending_and_nextVal):

	global tiles

	column = [[], [], [], []]

	(ending, nextVal) = ending_and_nextVal

	for index1 in range(4):

		for rows in tiles: column[index1].append(rows[index1])

		sPush(column[index1], ending, nextVal)

	tiles = [[], [], [], []]

	for index2 in range(4):

		for display in column: tiles[index2].append(display[index2])


def horizontal(ending_and_nextVal):

	global tiles

	fill = [] # fill = fill in for tiles

	(ending, nextVal) = ending_and_nextVal

	for rows in range(4): fill.append(sPush(tiles[rows], ending, nextVal))

	tiles = fill


def newTile(four):

	global tiles

	spawn = random.randint(1, 16) # Where to spawn next tile

	'''
	Assuming each tile had its own number (first tile has number 1, second tile has number 2... last tile has number 16), the last tile of each row is a multiple of 4 and
	and everything before in that row is less than that multiple, however, greater than the previous multiple. If we divide the spawn by 4, then we get a whole number for
	the last tile and slightly smaller numbers for the first 3 (still greater than the previous row). Therefore, if I ceiling round the number, we will get the row number.
	But since list index start with zero, I must minus by 1.
	'''

	index = int(ceil(spawn / float(4) - 1))

	# spawn - index * 4 - 1 converts the number assigned to each tile into values from 0 to 3. Therefore, after the row is found, the exact value can be found.

	replace = tiles[index][spawn - index * 4 - 1]

	possible = 95 / float(929) # probibility of getting a 4 out of one

	if replace != 0: newTile(four)

	elif 95 / float(929) >= four: tiles[index][spawn - index * 4 - 1] = 4

	elif 95 / float(929) < four: tiles[index][spawn - index * 4 - 1] = 2


def movement(group4): # checking if any moves are possible; the group of 4s i.e - rows or columns

	global same

	for check in group4:

		for numbers in range(3):

			if check[numbers] == check[numbers + 1]: same += 1


def output():

	for display in tiles:

		display = list(map(str, display))

		for null in range(4):

			if display[null] == '0': display[null] = ''

		print '|	' + '	|	'.join(display) + '\n'


tiles = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 2], [4, 8, 0, 0]]

function = {

'up': vertical,

'down': vertical,

'left': horizontal,

'right': horizontal

}

arguments = {
	
'up': (range(3), + 1),

'down': (range(3, 0, - 1), - 1),

'left': (range(3), + 1),

'right': (range(3, 0, - 1), - 1)

}

newTile(random.random()); newTile(random.random()) # game spawns 2 tiles at the beginning

while True:

	zero = False

	zero_num = same = 0 # zero_num = the amount of rows/columns that have no 0s

	prev = [[], [], [], []] # cannot reference prev and column as same object because lists are mutable so re-assignement changes both of them

	columns = [[], [], [], []]

	for rows in range(4):

		for numbers in tiles[rows]: prev[rows].append(numbers) # I can't just do prev = tiles[: ] because tiles is a gloabal vaiable

	output()

	direction = raw_input('Direction: ')

	function[direction](arguments[direction])

	for index in range(4):

		for rows in tiles: columns[index].append(rows[index])

	if prev != tiles: newTile(random.random()) # to check for any change

	movement(columns)

	movement(tiles)

	for check in tiles:

		if 0 not in check: zero_num += 1

	if zero_num == 4 and same == 0: break

	print '\n\n'

output()

print '\n\n' + 'Sorry, you lost!'
