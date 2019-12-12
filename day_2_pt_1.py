#test inputs
#input = [1,9,10,3,2,3,11,0,99,30,40,50]
#input = [1,1,1,4,99,5,6,0,99]
f = open("day_2_input.txt", "r")
nums = f.read()
nums = list(nums.replace("\n", "").split(","))
input_list = [int(n) for n in nums]
#print(input_list)
input_list[1] = 12
input_list[2] = 2
print(input_list[:3])


for i in range(len(input_list)):
	if (i % 4 == 0) and (input_list[i] == 99):
		print(input_list[0])
		print("program broke")
		break
	elif (i % 4 == 0) and (input_list[i] != 99):
		if input_list[i] == 1:
			add = input_list[input_list[i + 1]] + input_list[input_list[i + 2]]
			pos = input_list[i + 3]
			input_list[pos] = add 
			#print(input[pos])
		elif input_list[i] == 2:
			mult = input_list[input_list[i + 1]] * input_list[input_list[i + 2]]
			posit = input_list[i + 3]
			input_list[posit] = mult
			#print(input[posit])


	





