
class Location:
	def __init__(self, x,y):
		self.x = x    #instance variable unique to each instance
		self.y = y    #instance variable unique to each instance
  
facing = 'N'

start = Location(0,0)

f = open('R0.txt', 'r')
input = f.readline()

print (input)

commands = input.split(', ')

for entry in commands:
	command = entry[0]
	distance = int(entry[1:])
		
	if facing == "N":
		if command == "R":
			facing = 'E'
			start.x = start.x + distance
		elif command == "L":
			facing = 'W'
			start.x = start.x - distance
	elif facing == "E":
		if command == "R":
			facing = 'S'
			start.y = start.y - distance
		elif command == "L":
			facing = 'N'
			start.y = start.y + distance
	elif facing == "S":
		if command == "R":
			facing = 'W'
			start.x = start.x - distance
		elif command == "L":
			facing = 'E'
			start.x = start.x + distance
	elif facing == "W":
		if command == "R":
			facing = 'N'
			start.y = start.y + distance
		elif command == "L":
			facing = 'S'
			start.y = start.y - distance

	# print (distance)

	# print ('I am facing:', facing, start.x, start.y)
	
Distance_From_HQ = (abs(start.x) + abs(start.y))/2

print ('My distance from the East Bunny HQ you visit twice', Distance_From_HQ)

























