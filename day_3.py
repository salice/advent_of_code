f = open("day_3_input.txt", "r")
inputs = f.read()
split = inputs.split("\n")

input1 = split[0].split(",")
input2 = split[1].split(",")


def find_path(input_list):
	direction = [i[0] for i in input_list]
	magnitude = [int(i[1:]) for i in input_list]

	movement_dict = dict(zip(direction, magnitude))

	x = 0
	y = 0
	positions = []

	for i in movement_dict.keys():
		if i == "U":
			for j in list(range(1,movement_dict[i] + 1)):
				positions.append((x, y + j))
			y += movement_dict[i]
		elif i == "D":
			for j in list(range(1, movement_dict[i] + 1)):
				positions.append((x, y - j))
			y -= movement_dict[i]
		elif i == "R":
			for j in list(range(1, movement_dict[i] + 1)):
				positions.append((x + j, y))
			x += movement_dict[i]
		else:
			for j in list(range(1, movement_dict[i] + 1)):
				positions.append((x - j, y))
			x -= movement_dict[i]
	return positions


path1 = find_path(input1)
path2 = find_path(input2)
print(path1)
print(path2)

def find_min_intersection(list1, list2):
	intersections = []
	for i in list1:
		if i in list2:
			intersections.append(i)
	return [sum((tup)) for tup in intersections]

crosses = find_min_intersection(path1, path2)
print(crosses)

