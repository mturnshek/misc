import random

# longest run of a bernouilli sequence of length n
# with event A probability = pA
def longest_run(pA, n):
	iteration = 0
	max_run = 0
	run = 0
	while iteration < n:
		if random.random() < pA:
			run += 1
			if run > max_run:
				max_run = run
		else:
			run = 0
		iteration += 1
	return max_run

def average_longest_run(pA, n, num_generated_data):
	max_runs = []
	for i in xrange(num_generated_data):
		max_runs.append(longest_run(pA, n))
	average = float(sum(max_runs))/len(max_runs)
	return average

# example
# print average_longest_run(.95, 10000, 10000)
print average_longest_run(.5, 100, 10000)