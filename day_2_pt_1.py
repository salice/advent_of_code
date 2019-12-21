#test inputs
#input = [1,9,10,3,2,3,11,0,99,30,40,50]
#input = [1,1,1,4,99,5,6,0,99]
#read in input file 
f = open("day_2_input.txt", "r")
nums = f.read()
nums = list(nums.replace("\n", "").split(","))
input_list = [int(n) for n in nums]

#make changes to list specified in problem 
input_list[1] = 25
input_list[2] = 5

#loop through list
for i in range(len(input_list)):
	#checking every 4 values to see if it is 99 (break)
	if (i % 4 == 0) and (input_list[i] == 99):
		print(input_list[0])
		print("program broke")
		break
	#taking 1 and 0 and adding the following values in the list if 1 and mult if 2
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


	





