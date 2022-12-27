
from typing import Union

def map_split(input_: Union[list,tuple]):
	return map(int, input_.split('-'))

if __name__ == '__main__':

	with open('input.txt','r') as f:
		content = f.read().splitlines()

	count = 0
	for line in content:
		left, right = line.split(',')
		left_l, left_r = map_split(left)
		right_l, right_r = map_split(right)
		
		cond = [

			[
				left_l >= right_l,
				left_r <= right_r
			],

			[
				left_l <= right_l,
				left_r >= right_r
			]

		]

		print(line)
		# true if either list in cond is [True,True] or [False, False]
		if sum([True for sublist in cond if sum(sublist) in [0,2]]) > 0:
			count+=1
			print(count)
