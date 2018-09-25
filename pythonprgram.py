
def Tile(size, missed_location,start_row, start_col):
	#print(missed_location)
	row = start_row + size/2
	col = start_col + size/2
	if size == 2:
		temp = []
		for x,y in ((row-1,col-1),(row-1,col),(row,col-1),(row,col)):
			 if (x,y) != missed_location:
				 temp.append((x,y))	
		return [temp]
		
	tile_location = []
	if missed_location[0] < row and missed_location[1] < col: #2nd quad
		tile_location.append(((row-1,col),(row,col-1),(row,col)))
		quad2 = missed_location
		quad1 = tile_location[-1][0]
		quad3 = tile_location[-1][1]
		quad4 = tile_location[-1][2]
	elif missed_location[0] >= row and missed_location[1] < col: #3rd quad
		tile_location.append(((row-1,col-1),(row-1,col),(row,col)))
		quad3 = missed_location
		quad2 = tile_location[-1][0]
		quad1 = tile_location[-1][1]
		quad4 = tile_location[-1][2]
	elif missed_location[0] < row and missed_location[1] >= col: #1st quad
		tile_location.append(((row-1,col-1),(row,col-1),(row,col)))
		quad1 = missed_location
		quad2 = tile_location[-1][0]
		quad3 = tile_location[-1][1]
		quad4 = tile_location[-1][2]
	elif missed_location[0] >= row and missed_location[1] >= col: #4th quad
		tile_location.append(((row-1,col-1),(row-1,col),(row,col-1)))
		quad4 = missed_location
		quad2 = tile_location[-1][0]
		quad1 = tile_location[-1][1]
		quad3 = tile_location[-1][2]
	#print(tile_location)
		
	tile_location.extend(Tile(size/2,quad2,start_row,start_col))
	tile_location.extend(Tile(size/2,quad1,start_row,start_col+size/2))
	tile_location.extend(Tile(size/2,quad3,start_row+size/2,start_col))
	tile_location.extend(Tile(size/2,quad4,start_row+size/2,start_col+size/2))
	return tile_location
		
if __name__ == '__main__':
	n = 4
	missed_location = (3,2)
	result = Tile(n,missed_location,0,0)	
	print(*result,sep = '\n')
