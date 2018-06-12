def push(first, scape, ending, nextVal, repeat): # scape = landscape (horizontal and vertical) - pun

	for zero in ending:

		if scape[zero] == 0:

			scape[zero] = scape[zero + nextVal]

			scape[zero + nextVal] = 0

			repeat += 1

			if repeat < 5: push(first, scape, ending, nextVal, repeat)

	repeat = 0

	for same in ending:

		if scape[same] == scape[same + nextVal] and scape[same] != 0:

			scape[same] *= 2

			scape[same + nextVal] = 0

	if first: push(False, scape, ending, nextVal, 0) # repetition will occur if first = True always - example [64, 4, 2, 2] would equal [64, 8, 0, 0]

	return scape


def vertical(ending_and_nextVal):

	global tiles

	column = [[], [], [], []]

	(ending, nextVal) = ending_and_nextVal

	for index1 in range(4):

		for row in tiles: column[index1].append(row[index1])

		push(True, column[index1], ending, nextVal, 0)

	tiles = [[], [], [], []]

	for index2 in range(4):

		for display in column: tiles[index2].append(display[index2])


def horizontal(ending_and_nextVal):

	global tiles

	fill = [] # fill = fill in for tiles

	(ending, nextVal) = ending_and_nextVal

	for row in range(4): fill.append(push(True, tiles[row], ending, nextVal, 0))

	tiles = fill


tiles = [
[64,	64,		0,		0],
[2,		2,		4,		4],
[2,		2,		0,		8],
[64,	4,		0,		8]
]

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

while True:

	for display in tiles:

		display = list(map(str, display))

		print '	|'.join(display)

	direction = raw_input('Direction: ')

	function[direction](arguments[direction])
