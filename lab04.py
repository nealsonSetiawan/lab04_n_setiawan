#lab04
#Nealson Setiawan
from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return


def solveMaze(maze,startX,startY):
	s = Stack()
	x = startX
	y = startY
	s.push([x,y])
	maze[x][y] = s.size()
	c = 0 #counterForTriesToBeginning
	k = 1 #kounterForNumberOfTries

	
	while c < 4:
		if(maze[x-1][y]) != 'G' and ((maze[x-1][y]) !=  '+') and (isinstance(maze[x-1][y],int) == False): #W
			s.push([x-1,y])
			k = k+1
			maze[x-1][y] = k
			x = x-1
				
		elif(maze[x][y+1]) != 'G' and (maze[x][y+1]) !=  '+' and (isinstance(maze[x][y+1],int) == False): #S
			s.push([x,y+1])
			k=k+1
			maze[x][y+1] = k
			y = y+1

		elif(maze[x+1][y]) != 'G' and (maze[x+1][y]) != '+' and (isinstance(maze[x+1][y],int) == False): #E
			s.push([x+1,y])
			k=k+1
			maze[x+1][y] = k
			x = x+1

		elif(maze[x][y-1]) != 'G' and (maze[x][y-1]) !=  '+' and (isinstance(maze[x][y-1],int) == False): #N
			s.push([x,y-1])
			k=k+1
			maze[x][y-1] = k
			y = y-1


		
		else:
			if (x == startX and y == startY):
				c += 1
			if (s.size() == 1):
				return False
			elif (s.size() > 1):
				s.pop()
				x=s.peek()[0]
				y=s.peek()[1]
			
			
		if(maze[x][y-1]) == ('G') or  \
			(maze[x][y+1]) == ('G') or\
			(maze[x-1][y]) == ('G') or\
			(maze[x+1][y]) == ('G'): #check is G there?
				printMaze(maze)
				return True
	
	return False #if c > 4, which means after four direction != solution -> FALSE

maze = [
['+','+','+','+','+','+'],
['+',' ','+',' ',' ','G'],
['+',' ',' ','+','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

print(solveMaze(maze,4,4))