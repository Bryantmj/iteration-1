# Make a local change
# Make another local change
# Make a change from home

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def print_list(list):
	print ""

def add_one(list):
	# standard for loop with range
	for i in range (0, len(list)):
		list[i] += 1

		return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]

# filter patterns - a type of iteration

# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats ", names[i], "! You got a perfect score!"

# accumulation pattern - type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n
		
	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n
	return current_max

def alternating_sum(numbers):
	total = 0
	for i in range(0, len(numbers)):
		if i == 0 or i % 2 == 1:
			total += numbers[i]
		else:
			total -= numbers[i]

	return total

# def alternating_sum(numbers):
	# total = numbers[i]
	# for i in range(0, len(numbers)):
			# if i % 2 == 0:
				# total += numbers[i]
			# else:
				# total -= numbers[i]

		# return total

def sum_outside(numbers, min, max):
	total = 0
	for n in numbers:
		if not (min <= n and n < max):
			total += n
		
	return total

def count_close_remainder(numbers, divisor):
	count = 0
	for n in numbers:
		remainder = n % divisor
		if remainder <= 1 or remainder == divisor-1:
			count += 1

	return count

def double_down(numbers, target):
	result = [maybe_doubled(numbers[0], numbers[0], target)]
	for i in range(1, len(numbers)):
		result.append(maybe_doubled(numbers[0], numbers[1-1], target))

	return result

def maybe_doubled(n, prev_n, target):
	distance = abs(n - target)
	if n < prev_n or distance <= 3:
		return 2 * n

	return n

def standarad_deviation(n, numbers, mean):
	total = 0
	for n in numbers:
		total += n
		n / len(numbers) = mean
		numbers - mean = difference
		difference^2 = new_mean


