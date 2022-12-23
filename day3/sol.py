

import string
letters = string.ascii_lowercase + string.ascii_uppercase

if __name__ == "__main__":

	with open('input.txt','r') as f:
		content = f.readlines()

	# this is very funny	
	# print(list(map(chr, range(ord('a'), ord('z')+1))))
	letter_vals = { letter:val+1  for val, letter in enumerate(letters)}

	# Solution 1
	total=0
	for line in content:

		# strip() gives me a weird feeling
		line = line.partition('\n')[0]
		half = int(len(line)/2)

		start, end = line[:half], line[half:]
		common = set(start).intersection(set(end))
		assert len(common), 'the length of intersection is not zero'
		total += letter_vals[common.pop()]

	print(f"Solution 1: {total}")


	# Solution 2
	rucksacks = []
	group_size = 6
	total = 0
	for num, line in enumerate(content,1):

		line = line.partition('\n')[0]
		rucksacks.append(line)

		if num % group_size == 0:

			assert len(rucksacks) == group_size, 'rucksacks wrong size'

			group1, group2 = rucksacks[:int(group_size/2)], rucksacks[int(group_size/2):]
			
			# first attempt
			# [set(i).intersection(b) for i,b in zip(group1, group1[::-1])]

			common_g1 = set.intersection(*map(set,group1))
			common_g2 = set.intersection(*map(set,group2))			

			total += letter_vals[common_g1.pop()] + letter_vals[common_g2.pop()]
			# dump rucksacks
			rucksacks = []


	print(f"Solution 2: {total}")
