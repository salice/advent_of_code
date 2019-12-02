from math import floor

#read in downloaded file
path = "day_1_input.txt"
f = open(path, "r")
inputs = f.read()
inputs = inputs.replace("\n", ",").split(",")[0:-1]
input_masses = [int(i) for i in inputs]

#part 1 solution
def fuel_counter_upper(mass_list):
	masses = []
	for mass in mass_list:
		fuel_amt = floor(mass / 3) - 2
		if fuel_amt > 0:
			masses.append(fuel_amt)
		else:
			pass
	return masses
print(sum(fuel_counter_upper(input_masses)))

#part 2 solution
def fuel_counter_upper_pt2(mass_list):
	initial_output = fuel_counter_upper(mass_list)
	second_output = fuel_counter_upper(initial_output)
	third_output = fuel_counter_upper(second_output)
	fourth_output = fuel_counter_upper(third_output)
	fifth_output = fuel_counter_upper(fourth_output)
	sixth_output = fuel_counter_upper(fifth_output)
	seventh_output = fuel_counter_upper(sixth_output)
	eighth_output = fuel_counter_upper(seventh_output)
	ninth_output = fuel_counter_upper(eighth_output)

	return(sum(initial_output) + sum(second_output) + 
		sum(third_output) + sum(fourth_output)+ sum(fifth_output) 
		+ sum(sixth_output) + sum(seventh_output) + sum(eighth_output)
		+ sum(ninth_output))


print(fuel_counter_upper_pt2(input_masses))